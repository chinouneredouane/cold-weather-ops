#!/usr/bin/env python3
"""Generate MP3 narration for every lesson with the Kokoro neural voice (offline).

Optional tool — the site works without it (browser voice fallback).

Setup (once):
    python3 -m venv .tts && .tts/bin/pip install kokoro-onnx soundfile
    download kokoro-v1.0.int8.onnx and voices-v1.0.bin from
    https://github.com/thewh1teagle/kokoro-onnx/releases (model-files-v1.0)
Needs ffmpeg on the PATH.

Usage:
    .tts/bin/python tools/make_audio.py --model kokoro.onnx --voices voices.bin [--voice af_heart] [--lessons 1,2,5] [--jobs 4]
"""
import argparse
import json
import html
import os
import re
import subprocess
import sys
import tempfile
from concurrent.futures import ProcessPoolExecutor

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import importlib  # noqa: E402
import slides as slides_mod  # noqa: E402

COURSE = None


def load_course(name):
    global COURSE
    COURSE = importlib.import_module(f"courses.{name}").COURSE
    return COURSE

# Spoken forms for abbreviations and symbols (applied in order).
SPOKEN = [
    # aircraft performance courses (before the general rules: % MAC, V-speeds, distances)
    (r"% MAC", " percent M A C"), (r"V1\(MCG\)", "V one M C G"), (r"V1/VR", "V one to V R"), (r"\bVREF ?\+ ?(\d+)", r"V ref plus \1"),
    (r"\bVREF40\b", "V ref 40"), (r"\bVSR0\b", "V S R zero"), (r"\bVSR\b", "V S R"), (r"\bVMCG\b", "V M C G"), (r"\bVMCA\b", "V M C A"),
    (r"\bVMCL\b", "V M C L"), (r"\bVMU\b", "V M U"), (r"\bVLOF\b", "V lof"), (r"\bVTIRE\b", "V tyre"), (r"\bVEF\b", "V E F"),
    (r"\bVREF\b", "V ref"), (r"\bVR\b", "V R"), (r"\bV2\b", "V 2"), (r"\bTORA\b", "tora"), (r"\bTODA\b", "toda"), (r"\bASDA\b", "asda"),
    (r"\bTORR\b", "T O R R"), (r"\bTODR\b", "T O D R"), (r"\bASDR\b", "A S D R"), (r"\bTOR\b", "T O R"), (r"\bTOD\b", "T O D"), (r"\bASD\b", "A S D"),
    (r"\bLDA\b", "L D A"), (r"\bLDR\b", "L D R"), (r"\bPLTOW\b", "performance limited take-off weight"), (r"\bTOW\b", "take-off weight"),
    (r"\bLDW\b", "landing weight"), (r"\bLFLW\b", "landing field limit weight"), (r"\bCLD\b", "certified landing distance"),
    (r"\bFAS\b", "final approach speed"), (r"\bFRT\b", "flat-rating temperature"), (r"\bATM\b", "assumed temperature method"),
    (r"\bMRC\b", "M R C"), (r"\bLRC\b", "L R C"), (r"\bECON\b", "econ"), (r"\bCI\b", "C I"), (r"\bMCT\b", "M C T"), (r"\bMCP\b", "M C P"),
    (r"\bOAA\b", "obstacle accountability area"), (r"\bRESA\b", "resa"), (r"\bFPPM\b", "F P P M"), (r"\bDDS\b", "driftdown speed"),
    (r"\bODM\b", "operating data manual"), (r"\bAOM\b", "A O M"), (r"\bAEO\b", "all engines operating"), (r"\bKIAS\b", "knots indicated"),
    (r"\bRTO\b", "rejected take-off"), (r"\bL/D\b", "lift to drag"), (r"\bTALPA\b", "talpa"), (r"\bPI\b", "P I"), (r"\bOPT FL\b", "optimum flight level"),
    (r"CAT\.POL\.A\.(\d+)", r"cat pol A \1"), (r"\bCS 25\.(\d+)", r"C S 25, \1"), (r"\bCS-AWO\b", "C S A W O"), (r"\bCFM56-7B\b", "C F M 56, 7 B"),
    (r"\bCFM56\b", "C F M 56"), (r"\bCFM\b", "C F M"), (r"\bPW150A\b", "P W 150 A"), (r"\bPW123\b", "P W 123"), (r"\bDHC-8-402\b", "D H C 8, 402"),
    (r"\bQ200\b", "Q 200"), (r"\bFL(\d{3})\b", r"flight level \1"), (r"\bM0\.(\d+)", r"Mach point \1"), (r"(\d)\s?lb\b", r"\1 pounds"),
    (r"(\d)\s?kg\b", r"\1 kilograms"), (r"\bhPa\b", "hectopascals"), (r"\brpm\b", "R P M"), (r"\bmph\b", "miles per hour"), (r"\bNM\b", "nautical miles"),
    (r"\bCAT (III|II|I)\b", lambda m: "cat " + {"I": "one", "II": "two", "III": "three"}[m.group(1)]), (r"\b2D\b", "2 D"), (r"\b3D\b", "3 D"),
    (r"\bMMEL\b", "master M E L"), (r"\bCDL\b", "C D L"), (r"\bRAIM\b", "raim"), (r"\bSBAS\b", "S-bas"), (r"\bGNSS\b", "G N S S"),
    (r"\bAIRAC\b", "air-rack"), (r"\bLPV\b", "L P V"), (r"\bLP\b", "L P"), (r"\bLNAV\b", "L NAV"), (r"\bRVR\b", "R V R"), (r"\bCMV\b", "C M V"),
    (r"\bOCA/H\b", "O C A or H"), (r"\bFALS\b", "fals"), (r"\bIALS\b", "I A L S"), (r"\bBALS\b", "balls"), (r"\bNALS\b", "nals"),
    (r"\bLVP\b", "L V P"), (r"\bLVTO\b", "L V T O"), (r"\bSARPs\b", "sarps"), (r"\bPANS\b", "pans"), (r"\bAMC\b", "A M C"), (r"\bGM\b", "G M"),
    (r"\bATA\b", "A T A"), (r"\bOM ([A-D])\b", r"O M \1"), (r"\bNOTOC\b", "no-tock"), (r"\bFTL\b", "F T L"), (r"\bAOC\b", "A O C"),
    (r"\bEFB\b", "E F B"), (r"\+TSRA", "heavy thunderstorm with rain"), (r"\bTS\b", "T S"), (r"\bWS R26\b", "windshear runway 26"),
    (r"Part-(ARO|ORO|CAT|SPA|FCL)", lambda m: "Part " + " ".join(m.group(1))), (r"\bAIP\b", "A I P"),
    (r"\b(ACAS|TCAS) II\b", r"\1 two"), (r"CAT\.IDE\.A\.(\d+)", r"CAT I D E A \1"), (r"\bSPA\.RVSM\b", "S P A R V S M"),
    (r"\bRVSM\b", "R V S M"), (r"\bCPDLC\b", "C P D L C"), (r"\bPM-CPDLC\b", "protected mode C P D L C"), (r"\bMASPS\b", "mass-ps"),
    (r"\bEGPWS\b", "E G P W S"), (r"\bGPWS\b", "G P W S"), (r"\bTAWS\b", "tawss"), (r"\bCFIT\b", "see-fit"), (r"\bCDFA\b", "C D F A"),
    (r"\bCANPA\b", "canpa"), (r"\bMSA\b", "M S A"), (r"\bMORA\b", "mora"), (r"\bMDA\b", "M D A"), (r"DA/H", "D A or H"), (r"MDA/H", "M D A or H"),
    (r"\bNTOP\b", "N top"), (r"\bMTOP\b", "M top"), (r"V<sub>GA</sub>|\bVGA\b", "V G A"), (r"\bLOFT\b", "loft"), (r"\bZFW\b", "Z F W"),
    (r"\bITT\b", "I T T"), (r"\bACAS\b", "ay-cass"), (r"\bTCAS\b", "tee-cass"), (r"\bRAs?\b", "R A"), (r"\bTA/RA\b", "T A, R A"), (r"\bAVSA\b", "A V S A"),
    (r"\bSSR\b", "S S R"), (r"\bCFL\b", "cleared flight level"), (r"\bDLIC\b", "D L I C"), (r"\bACM\b", "A C M"), (r"\bACL\b", "A C L"),
    (r"\bAMC\b", "A M C"), (r"\bDCL\b", "D C L"), (r"\bDSC\b", "D S C"), (r"\bCMU-900\b", "C M U 900"), (r"\bLSK 6R\b", "line select key 6 right"),
    (r"\bCDU\b", "C D U"), (r"\bATN\b", "A T N"), (r"\bATSU?\b", "A T S unit"), (r"\bANSPs?\b", "air navigation service provider"), (r"\bGOLD\b", "gold"),
    (r"\bDRSA\b", "D R S A"), (r"\bBLSA\b", "B L S A"), (r"\bSS / DS\b", "S S or D S"), (r"\bTCU\b", "T C U"), (r"\bCB\b", "C B"),
    (r"\bDACM\b", "D A C M"), (r"\bTRI/TRE\b", "T R I or T R E"), (r"\bFCU/MCP\b", "F C U or M C P"), (r"\bLNAV/VNAV\b", "L NAV V NAV"),
    (r"\bWAT\b", "weight altitude temperature"), (r"\bAIP\b", "A I P"), (r"\bFPA\b", "F P A"), (r"\bLVO\b", "L V O"), (r"\bPBN\b", "P B N"), (r"\bRNAV\b", "R NAV"),
    (r"\bAFDS\b", "A F D S"), (r"\bAAL\b", "above aerodrome level"), (r"\bAFE\b", "above field elevation"), (r"\bTDZ\b", "touchdown zone"),
    (r"\bRETILs?\b", "rapid exit taxiway indicator lights"), (r"\bSMGCS\b", "S M G C S"), (r"\bOFZ\b", "O F Z"), (r"\bILS\b", "I L S"),
    (r"\bSVR\b", "S V R"), (r"\bNNCs?\b", "non-normal checklists"), (r"\bADIRUs?\b", "A D I R U"), (r"\bDEUs?\b", "D E U"), (r"\bEFIS\b", "ee-fiss"),
    (r"\bAWO\b", "all weather operations"), (r"TO/GA", "toga"), (r"\bA/Ps\b", "autopilots"), (r"\bA/P\b", "autopilot"), (r"\bA/T\b", "autothrottle"),
    (r"\bOEI\b", "one engine inoperative"), (r"µ > 0\.3", "friction coefficient above 0 point 3"), (r"\bPFDs?\b", "P F D"), (r"\bAPU\b", "A P U"),
    (r"ft/min", "feet per minute"), (r"\bLOC\b", "localizer"), (r"\bG/S\b", "glideslope"), (r"\bGS\b", "glideslope"), (r"\bOM\b", "outer marker"),
    (r"\bPLI\b", "pitch limit indicator"), (r"\bAHRS\b", "A H R S"), (r"\bMFD\b", "M F D"), (r"\bND\b", "navigation display"),
    (r"\bDTPs?\b", "D T P"), (r"\bWOCL\b", "W O C L"), (r"\bFDP\b", "F D P"), (r"\bCFMU\b", "C F M U"), (r"\bIFPS\b", "I F P S"), (r"\bAFTN\b", "A F T N"), (r"\bSITA\b", "seeta"), (r"\bQAN\b", "Q A N"), (r"\bQFE\b", "Q F E"), (r"\bQNH\b", "Q N H"), (r"\bMTOW\b", "maximum take-off weight"), (r"\bFIR\b", "F I R"), (r"\bDAAA\b", "D A A A"), (r"(\d+) h (\d\d)\b", r"\1 hours \2"),
    (r"\bANAC\b", "A N A C"), (r"www\.anac\.dz", "the ANAC website"),
    (r"\bVMBE\b", "V M B E"), (r"V<tspan[^>]*>MBE</tspan>", "V M B E"), (r"\bEOSID\b", "engine-out SID"), (r"\bMTOM\b", "maximum take-off mass"), (r"\bSIDs?\b", "sid"),
    (r"\bG-HRCs?\b", "global high-risk categories"), (r"\bGASP\b", "gasp"), (r"\bIATA\b", "eye-ah-ta"), (r"\bFSF\b", "Flight Safety Foundation"), (r"\bFOQA\b", "foqua"), (r"\bFDM\b", "F D M"), (r"\bMSAWS?\b", "M SAW"), (r"\beTOD\b", "e T O D"), (r"\bMAC\b", "mid-air collision"), (r"\bNASPs?\b", "N A S P"), (r"\bCBTA\b", "C B T A"), (r"\bPNF\b", "pilot not flying"), (r"\bNPAs?\b", "non-precision approach"), (r"\bUAS\b", "undesired aircraft state"), (r"\bRE\b", "runway excursion"), (r"\bRI\b", "runway incursion"),
    (r"\bWILCO\b", "wilco"), (r"\bAFFIRM\b", "affirm"), (r"\bSTANDBY\b", "standby"), (r"\bUNABLE\b", "unable"),
    (r"\s*\(kt\)", " in knots"),
    (r"VS\(n\) = VS × √n", "the stall speed at load factor n equals the normal stall speed times the square root of n"),
    (r"\bLOC-I\b", "loss of control in flight"), (r"\bUPRT\b", "U P R T"), (r"\bFSTDs?\b", "simulator"),
    (r"\bAUPRTA\b", "the upset training aid"), (r"\bPANS-TRG\b", "pans T R G"), (r"\bMPL\b", "M P L"),
    (r"\bCS-25\b", "C S 25"), (r"\bFAR Part 25\b", "F A R part 25"), (r"\bFCTM\b", "F C T M"), (r"\bFMA\b", "F M A"),
    (r"\bPFD\b", "P F D"), (r"\bPF\b", "pilot flying"), (r"\bPM\b", "pilot monitoring"), (r"\bCG\b", "C G"),
    (r"\bGPS\b", "G P S"), (r"\bFD\b", "flight director"), (r"\bA300-600\b", "A 300, 600"), (r"\bA330-200\b", "A 330, 200"),
    (r"\bA320\b", "A 320"), (r"\bQ400\b", "Q 400"), (r"\bB737-800\b", "Boeing 737, 800"), (r"Boeing 737-800", "Boeing 737, 800"),
    (r"V(MO|D|A|FE|LE|LO|S1g|SR|S)\b", lambda m: "V " + " ".join(m.group(1).replace("1g", " 1 g"))),
    (r"\bM(MO|D)\b", lambda m: "M " + " ".join(m.group(1))),
    (r"(\d(?:\.\d)?) g\b", r"\1 g"), (r"([+−-])(\d(?:\.\d)?) g", lambda m: ("plus " if m.group(1) == "+" else "minus ") + m.group(2) + " g"),
    (r"θ = γ \+ α", "pitch equals flight path angle plus angle of attack"), (r"\(θ\)|\(γ\)|\(α\)", ""),
    (r"n = 1 ?/ ?cos\(?bank(?: angle)?\)?", "n equals one over the cosine of the bank angle"),
    (r"\+(\d)", r"plus \1"), (r" = ", " equals "),
    (r"(\d)\.(\d)", r"\1 point \2"),
    (r"Lift = ½ × ρ × V² × S × CL", "lift equals one half, times air density, times speed squared, times wing area, times the lift coefficient"),
    (r"\be\.g\.", "for example"), (r"\bi\.e\.", "that is"), (r"\betc\.", "and so on"),
    (r"(\d)\s?°C", r"\1 degrees"), (r"°C", "degrees"), (r"°", " degrees"),
    (r"−|–(?=\d)", "minus "), (r"≈", "approximately "), (r"≤", "at most "), (r"√", "the square root of "),
    (r"×", " times "), (r"→", ", "), (r"·", ", "), (r"—|–", ", "),
    (r"(\d)\s?%", r"\1 percent"), (r"(\d)\s?mm\b", r"\1 millimetres"), (r"(\d)\s?ft\b", r"\1 feet"),
    (r"(\d)\s?kt\b", r"\1 knots"), (r"(\d)\s?m\b", r"\1 metres"), (r"(\d)\s?psi\b", r"\1 P S I"),
    (r"(\d) (\d{3})\b", r"\1\2"),                         # 1 600 -> 1600
    (r"\b100/0\b", "one hundred, zero"), (r"\b75/25\b", "seventy-five, twenty-five"), (r"\b50/50\b", "fifty-fifty"),
    (r"\b5/5/2\b", "five, five, two"),
    (r"XXXX 01170830 09 5/5/2 100/100/50 NR/NR/06 WET/WET/SLUSH", ""),
    (r"\bHOTs?\b", "holdover time"), (r"\bRWYCC\b", "runway condition code"), (r"\bRCR\b", "runway condition report"),
    (r"\bRCAM\b", "R CAM"), (r"\bGRF\b", "G R F"), (r"\bPTCC\b", "P T C C"), (r"\bCSFF\b", "C S F F"),
    (r"\bLOUT\b", "L O U T"), (r"\bAFMs?\b", "A F M"), (r"\bFCOM\b", "F COM"), (r"\bQRH\b", "Q R H"),
    (r"\bMEL\b", "M E L"), (r"\bCDL\b", "C D L"), (r"\bOAT\b", "O A T"), (r"\bTAT\b", "T A T"), (r"\bISA\b", "I S A"),
    (r"\bSLD\b", "S L D"), (r"\bAoA\b", "angle of attack"), (r"\bAPU\b", "A P U"), (r"\bATC\b", "A T C"),
    (r"\bCRM\b", "C R M"), (r"\bTEM\b", "T E M"), (r"\bSMS\b", "S M S"), (r"\bRTO\b", "R T O"), (r"\bFPD\b", "F P D"),
    (r"\bFMS\b", "F M S"), (r"\bMSA\b", "M S A"), (r"\bDA/MDA\b", "D A or M D A"), (r"\bRNP\b", "R N P"),
    (r"\bLNAV/VNAV\b", "L NAV, V NAV"), (r"\bbaro-VNAV\b", "baro V NAV"), (r"\bEGT\b", "E G T"),
    (r"\bN1/N2\b", "N one and N two"), (r"\bN2/N1\b", "N two and N one"), (r"\bN1\b", "N one"), (r"\bN2\b", "N two"),
    (r"\bTAF\b", "taff"), (r"\bMETAR\b", "mee-tar"), (r"\bNOTAMs?\b", "NO-tam"), (r"\bSNOWTAM\b", "snow-tam"),
    (r"\bATIS\b", "ay-tis"), (r"\bICAO\b", "I CAO"), (r"\bEASA\b", "ee-ah-sah"), (r"\bFAA\b", "F A A"),
    (r"\bSAE\b", "S A E"), (r"\bPANS-OPS\b", "pans ops"), (r"\bCFR\b", "C F R"), (r"\bAC\b(?= 120)", "advisory circular"),
    (r"\bCAT\.OP\.MPA\.(\d+)", r"CAT O P M P A \1"), (r"\bAMS(\d+)", r"A M S \1"), (r"\bAS(\d+)", r"A S \1"),
    (r"\bCLmax\b", "C L max"), (r"\bCL\b", "C L"), (r"\bV1\b", "V one"), (r"\bVP\b|VP\b", "V P"),
    (r"\bTCAS\b", "tee-cas"), (r"\bPIC\b", "pilot in command"), (r"\bPA\b", "P A"), (r"\bFLEX\b", "flex"),
    (r"\bUTC\b", "U T C"), (r"\bNR\b", "not reported"), (r"\bCAT II/III\b", "category two or three"),
    (r"\bFZRA\b", "F Z R A"), (r"\bFZDZ\b", "F Z D Z"), (r"\bFZFG\b", "F Z F G"), (r"\bBLSN\b", "B L S N"),
    (r"\bSN\b", "S N"), (r"\bSG\b", "S G"), (r"\bPL\b", "P L"), (r"\bGR\b", "G R"), (r"\bGS\b", "G S"),
    (r"\bBR\b", "B R"), (r"\bPROB\b", "prob"), (r"\bBECMG\b", "becoming"), (r"\bTEMPO\b", "tempo"),
    (r"\bB737-700\b", "Boeing seven three seven, seven hundred"), (r"\bB737-200\b", "Boeing seven three seven, two hundred"),
    (r"\bMD-81\b", "M D eighty-one"), (r"\bMD-80\b", "M D eighty"), (r"\bF28\b", "F twenty-eight"),
    (r"\bATR 72\b", "A T R seventy-two"), (r"\bBA38\b", "B A thirty-eight"), (r"\bCRJ\b", "C R J"),
    (r"Type I\b", "Type one"), (r"Type II\b", "Type two"), (r"Type III\b", "Type three"), (r"Type IV\b", "Type four"),
    (r"Types I, II, III and IV", "Types one, two, three and four"), (r"Types II, III and IV", "Types two, three and four"),
    (r"Types II and IV", "Types two and four"), (r"\bII/IV\b", "two and four"), (r"\bII/III/IV\b", "two, three and four"),
    (r"\bI and II\b", "one and two"), (r"\(I, II, III or IV\)", ""),
    (r"\s*/\s*", " or "),
]


def to_speech(html_text):
    t = re.sub(r"<figure\b.*?</figure>", lambda m: " " + slides_mod.caption_speech(m.group(0)) + " ", html_text, flags=re.S)
    t = re.sub(r'<div class="dialog".*?</div>', " ", t, flags=re.S)
    t = re.sub(r'<p class="muted">Example only.*?</p>', " ", t, flags=re.S)
    t = re.sub(r"<(sub|sup)>(.*?)</\1>", r"\2", t)
    t = re.sub(r"</(td|th)>", ". ", t)
    t = re.sub(r"</(p|li|h2|h3|tr|div|table|ol|ul)>", ". ", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t)
    t = re.sub(r"\s*\((?:see )?(?:the )?[^()]*Lesson \d+[^()]*\)", "", t)   # cross-references
    t = re.sub(r"\s*\([A-Z][A-Za-z0-9]{1,6}\)", "", t)                       # "(HOT)", "(RWYCC)"
    for pat, rep in SPOKEN:
        t = re.sub(pat, rep, t)
    t = re.sub(r"[;:]\s", ". ", t)
    t = re.sub(r"[()\"“”‘’]", " ", t)
    t = re.sub(r"\s+", " ", t)
    t = re.sub(r"[,;:]\s*\.", ".", t)
    t = re.sub(r"(\s*\.\s*)+", ". ", t)
    t = re.sub(r"\s+([,.!?])", r"\1", t)
    return t.strip(" .") + "."


def lesson_script(n):
    if COURSE is None:
        load_course("cold_weather")
    L = COURSE["lessons"][n - 1]
    parts = [f"Lesson {n}. {L['title']}.", "Learning objectives. " + " ".join(L["objectives"]), L["body"],
             "Key takeaways. " + " ".join(L["takeaways"])]
    return to_speech(" ".join(f"<p>{p}</p>" for p in parts))


def slide_scripts(n):
    """Speech text per slide, in the order the slide player shows them (objectives + intro, sections, takeaways)."""
    if COURSE is None:
        load_course("cold_weather")
    L = COURSE["lessons"][n - 1]
    intro, body = slides_mod.body_slides(L["body"])
    out = [to_speech(f"<p>Lesson {n}. {L['title']}.</p><p>Learning objectives. {' '.join(L['objectives'])}</p>{intro}")]
    for _t, h in body:
        h = re.sub(r"<h2>[^<]*\(\d+\)</h2>", "", h)          # continuation slide: do not read the title again
        out.append(to_speech(h.replace("<h2>", "<p>").replace("</h2>", "</p>")))
    out.append(to_speech("<p>Key takeaways. " + " ".join(L["takeaways"]) + "</p>"))
    return out


def sentences(text, limit=300):
    out, cur = [], ""
    for s in re.findall(r"[^.!?]+[.!?]", text):
        s = s.strip()
        if not s:
            continue
        if len(cur) + len(s) > limit and cur:
            out.append(cur)
            cur = s
        else:
            cur = (cur + " " + s).strip()
    if cur:
        out.append(cur)
    return out


def render(args):
    n, model, voices, voice, speed, outdir, course = args
    load_course(course)
    import numpy as np
    import soundfile as sf
    from kokoro_onnx import Kokoro
    k = Kokoro(model, voices)
    pieces = []
    sr = 24000
    cues, length = [], 0
    for text in slide_scripts(n):                    # each slide starts a new sentence group -> exact slide cues
        cues.append(round(length / sr, 2))
        for chunk in sentences(text):
            samples, sr = k.create(chunk, voice=voice, speed=speed, lang="en-us")
            pieces.append(samples)
            pieces.append(np.zeros(int(sr * 0.35), dtype=samples.dtype))
            length += len(samples) + int(sr * 0.35)
    audio = np.concatenate(pieces)
    with open(os.path.join(outdir, f"lesson-{n:02d}.cues.json"), "w", encoding="utf-8") as f:
        json.dump(dict(duration=round(len(audio) / sr, 2), cues=cues + [None], source="recording"), f)
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
        sf.write(tmp.name, audio, sr)
        out = os.path.join(outdir, f"lesson-{n:02d}.mp3")
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", tmp.name, "-ac", "1", "-ar", "24000",
                        "-codec:a", "libmp3lame", "-b:a", "48k", "-metadata", f"title=Lesson {n}: {COURSE['lessons'][n-1]['title']}",
                        "-metadata", "artist=Domestic Airlines Training", out], check=True)
        os.unlink(tmp.name)
    return n, len(audio) / sr


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True)
    ap.add_argument("--voices", required=True)
    ap.add_argument("--voice", default="af_heart")
    ap.add_argument("--speed", type=float, default=1.0)
    ap.add_argument("--lessons", default="")
    ap.add_argument("--jobs", type=int, default=2)
    ap.add_argument("--print-script", type=int, default=0, help="print the spoken text of one lesson and exit")
    ap.add_argument("--course", default="cold_weather", help="course package under tools/courses (e.g. upset_recovery)")
    a = ap.parse_args()
    load_course(a.course)
    if a.print_script:
        print(lesson_script(a.print_script))
        return
    nums = [int(x) for x in a.lessons.split(",") if x] or list(range(1, len(COURSE["lessons"]) + 1))
    outdir = os.path.join(ROOT, "courses", COURSE["slug"], "media", "audio")
    os.makedirs(outdir, exist_ok=True)
    jobs = [(n, a.model, a.voices, a.voice, a.speed, outdir, a.course) for n in nums]
    with ProcessPoolExecutor(max_workers=a.jobs) as ex:
        for n, secs in ex.map(render, jobs):
            print(f"lesson {n:02d}: {secs/60:.1f} min", flush=True)


if __name__ == "__main__":
    main()

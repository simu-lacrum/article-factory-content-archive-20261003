---
source: melonity-knowledge-base.md
heading: "3A.6.1. Client-side bypass"
---

#### 3A.6.1. Client-side bypass

VAC сканирует процесс игры в поисках «чужого» кода. Что VAC проверяет:
- Целостность файлов игры (CRC checks)
- Loaded modules (DLLs загруженные в процесс)
- Memory regions (поиск signature patterns известных читов)
- Open handles to game process (кто читает память Dota 2)
- Thread start addresses (`NtQueryInformationThread` каждый thread attach event)

**Как cheats обходят:**
- **Manual mapping** — DLL не loaded в стандартный module list (нет entry в loaded modules)
- **Process hiding** — подмена имени процесса/PID
- **File renaming after launch** — VAC запоминает initial file identifier, после запуска можно переименовать
- **Delayed injection** — ждут 5 мину�� после старта Dota (после первых 5 минут VAC сканит каждые 3 минуты, до того — каждую секунду при неактивном окне)
- **HWID Spoofer** — меняет hardware fingerprint (motherboard SN, BIOS UUID, disk serial, MAC, GPU ID) — защита от HWID-ban

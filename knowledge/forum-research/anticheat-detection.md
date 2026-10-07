# Анти-читы и детекты: фактура с форумов и блогов

> Для пересказа своими словами. Каждый пункт — с URL. «сниппет» = прочитан только сниппет поиска.
> Инструкции по обходу не берём — только механика и аналитика.

## VAC / VACnet / VAC Live (Valve)
- **История VAC**: с 2002 (Counter-Strike), ранние версии — сигнатурный скан памяти/процессов +
  challenge-ответы клиента; VAC2 (2005) сделал баны перманентными. Wikipedia — **сниппет**.
  https://en.wikipedia.org/wiki/Valve_Anti-Cheat
- **VACnet** (анонс GDC 2018) — ML-половина VAC: смотрит не «что установлено», а «как ты играешь».
  На каждый выстрел берёт окно ~0.5с до и ~0.25с после, меряет изменение pitch/yaw + контекст (оружие,
  дистанция, попал ли) — «atom». Последовательность из 140 атомов за 8 раундов подаётся в модель,
  которая оценивает вероятность «обвинительного» вердикта Overwatch-ревьюера. Тренировалась на вердиктах
  Overwatch; 1700 CPU у Valve. Начинали именно с аимботов: аимбот выдаёт себя в предсказуемый момент —
  нажатие на курок, вокруг которого и строится окно. https://vac-ban.com/wiki/vacnet — **сниппет**
- **VAC Live** — боевой слой VACnet в CS2: действует во время матча (отмена игры, кулдаун, бан на месте).
  Строки "Cheater Detected" / "This match has been canceled by VAC Live" датамайнеры нашли ещё до анонса.
  Два исхода: перманентный VAC (точная идентификация софта) ИЛИ отмена матча + кулдаун при «нерегулярной»
  игре (не значит бан). Сама Valve в документации называет VAC Live «системой, ранее известной как VACnet».
  https://vac-ban.com/wiki/vac-live — **сниппет**
- **Практика детекта (UC)**: сообщают, что летом 2025 VAC Live резко «поумнел» — ловит блатантную игру
  (высокий HS%, килы через дым/стены) за несколько раундов даже у external без записи памяти (автор треда
  до этого ~500 часов играл без проблем, теперь получает кулдаун в пределах матча); «closet»
  (аккуратный) чит пока не триггерит. https://www.unknowncheats.me/.../708645-...rounds.html — **сниппет**
- **Что считают игроки-девелоперы причиной флага (UC 750674)**: привязка к trust factor / non-prime +
  флаг IP/HWID; фикс. частота ввода у external — красный флаг; прямая запись viewangles — сильный флаг
  серверной стороны; совет не «локать сквозь стены», рандомизировать smooth, держать «человеческий»
  input rate (по их словам, на non-prime с флагнутым IP/HWID банит быстрее). Это мнения практиков,
  не подтверждённая механика. https://www.unknowncheats.me/.../750674-vac-live-detections.html — **сниппет**
- **cs2-vac-internals** (Aspasia1337): заметки и код по внутренностям VAC в CS2 — база для техврезки.
  https://github.com/Aspasia1337/cs2-vac-internals — **сниппет**

## Riot Vanguard (эталон kernel-AC, для сравнений)
- **Dispatch-table хуки** (Archie, 2025): Vanguard ставит хуки по всему ядру; таблица в .data (writable,
  не под PatchGuard), хук в SwapContext управляется битом в nt!KiCpuTracingFlags (логирование сисколлов
  также через KiDynamicTraceMask); перехват сисколлов через HalCollectPmcCounters (метод Khoury/Daax) и
  HalClearLastBranchRecordStack. https://archie-osu.github.io/2025/04/11/vanguard-research.html — **сниппет**
- **IAT-хук vgk.sys** (gmh5225): VGK грузится раньше остальных, перехватывает загрузку всех последующих
  драйверов и хукает их IAT на опасные функции (напр. MmCopyVirtualMemory), поэтому Ring0 чтение/запись
  памяти игры падает; не inline-hook, т.е. не триггерит PatchGuard. https://gist.github.com/gmh5225/2b430b6025c8888196dd95c8557bfc6f — **сниппет**
- **Page-fault детект manual-map** (0avx): ставит execute-disable на отслеживаемые PTE; попытка исполнения
  из неавторизованной страницы → #PF → хук KiPageFault логирует страницу/оффсет; аккуратно обходит
  контекст PatchGuard. https://github.com/0avx/0avx.github.io/blob/main/article-5.md — **сниппет**
- **VanguardTrace** (armvirus): расшифровка/перехват зашифрованных импортов vgk.sys, сигнатурный поиск
  таблицы. https://github.com/armvirus/VanguardTrace — **сниппет**
- **Guarded Regions** (Xyrem/reversing.info): shadow PML4 / переключение таблиц страниц в SwapContext —
  память игры (World/Engine/Names) недоступна невайтлистнутым процессам. https://reversing.info/posts/guardedregions/ — **сниппет**

## Easy Anti-Cheat (EAC/EOS)
- Сервис + kernel-драйвер + per-game модуль; драйвер регистрирует process/thread/image-load/registry/
  debug-print/NMI колбэки + FLTMGR фильтрацию; мониторит модули/драйверы, хэндлы, память, kernel-патчи,
  целостность сертификатов/каталогов. Ядро логики — под кастомной VM, статика видит только поверхность;
  динамика (revhv) восстанавливает внешние call-paths. Анти-дебаг, hypervisor/VM тайминги, MSR-пробы.
  https://github.com/goldzik1/eac-eos-driver-analysis · https://life45.github.io/blog/dynamic-analysis-with-revhv/ ·
  https://www.unknowncheats.me/forum/anti-cheat-bypass/749306-easyanticheat_eos-sys-startup.html · https://github.com/adrianyy/EACReversing — **сниппет**

## BattlEye
- **BEClient** — DLL в процессе игры, большая часть детекта и связь с сервером; экспортит GetVer/Init,
  Init под VMProtect. Публичные разборы: скан аномалий executable-памяти, pattern-scan, проверки
  модулей/процессов/окон, hypervisor-тайминги, целостность report-таблицы. Новый разбор (EFT): AES-128
  inverse-cipher, 60-сек цикл валидации, LCG PRNG в BEClient_x64.dll. Денилист уязвимых драйверов по
  timestamp, детект DSE-обходов. secret.club (2019/2020) + https://www.unknowncheats.me/.../736294-battleye-beclient_x64-dll-analysis-eft.html — **сниппет**

## FACEIT AC
- Boot-time kernel-драйвер; process/thread/image колбэки, мониторинг хэндлов, блокировка уязвимых
  драйверов, детект VM/Hyper-V, требования TPM/Secure Boot/DEP, серверный поведенческий анализ.
  Исторический HWID: первый серийник диска + MAC локальной NIC (логируется). VMProtect мешает реверсу.
  https://www.unknowncheats.me/.../258402-faceit-ac-hardware-logging.html · https://arxiv.org/html/2408.00500v1 — **сниппет**

## Общая механика kernel-AC и manual-map
- Детект manual-mapped драйверов: executable-память вне известных модулей, скан pool/big-pool,
  NMI-сэмплинг стека, паттерны компилятора/импортов, проверки целостности образа. Tulach + s4dbrd —
  хорошая база для обзорной статьи «как работают kernel-античиты». https://tulach.cc/detecting-manually-mapped-drivers/ ·
  https://s4dbrd.github.io/posts/how-kernel-anti-cheats-work/ — **сниппет**

## Deadlock (встроенный анти-чит Valve)
- **Интегрити-чеки (UC 729952, прочитано)**: в `game/bin/win64/citadel.signatures` лежат SHA1/CRC32 для
  бинарей игры; читает их сам deadlock.exe. Без `-insecure` (или с `-tools`) игра детурит NtOpenFile
  (ntdll), LoadLibraryExW (kernelbase), PeekMessageW (user32) из функции, вызываемой в WinMain сразу
  после парсинга аргументов. https://www.unknowncheats.me/forum/deadlock/729952-deadlocks-built-anticheat-diagnostics-system.html — **прочитано**
- **Статус VAC в Deadlock (UC 745313)**: сообщается, что VAC-модули отключены, активны только проверки
  списка DLL / vtable; manual-map обходит PEB-энумерацию модулей. https://www.unknowncheats.me/forum/deadlock/745313-anti-cheat-systems-deadlock.html — **сниппет**
- **Диагностика по сети**: protobuf-сообщения вида CUserMessage_DllStatus (сбор списка модулей,
  подписи DLL, HWID). https://github.com/ianveig29/how-vac-works — **сниппет**

## Trust Factor и волны банов
- **Trust Factor** — скрытый аккаунт-скор матчмейкинга (плейтайм, репорты, активность в других Steam-играх;
  веса не публикуются). Prime — отдельная система. https://blog.counter-strike.net/the-trust-factor/ — **сниппет**
- **Волны банов CS2 2024**: 27 апр 2024 — ~130–158 VAC + 64 game-bans (после возврата Overwatch 25–26 апр);
  начало мая — крупнее (CSStats ~26k 8 мая; трекеры >300k к 30 мая). Трекер истории: vac-ban.com/ban-history.
  https://dotesports.com/counter-strike/news/hope-springs-eternal-new-cs2-vac-ban-wave-has-community-hyped — **сниппет**

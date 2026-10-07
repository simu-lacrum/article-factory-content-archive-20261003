# Forum research — INDEX (темы с уникальной фактурой для статей)

Собрано: **2026-10-07**. Источники: unknowncheats.me, yougame.biz, профильные блоги/GitHub/академия.
Всего тем: **42** (включая кластер colby57). Детали по крупным темам: `colby57.md`,
`anticheat-detection.md`, `cheat-internals.md`. Полный список ссылок: `sources.csv`.

**Статусы:** `прочитано` = открыл страницу целиком; `сниппет` = только сниппет поиска (полный текст под
Cloudflare/логином — пометил в разделе «не удалось открыть»). Оффсеты/числа протухают — ценность в механике.
Факты не выдумывались: каждый — с URL. Большие куски текста не копировались (лицензии) — пересказ/короткие цитаты.

Сайты: **melonity.gg**/**dota2cheat.com** = Dota 2; **cluster.center** = CS2/Deadlock external;
**deadlockhacks.com** = Deadlock; **cheatsgaming.com** = общие читы/анти-читы/реверс; **metaskins.gg** = скины.

| # | Тема | Автор | Дата | Игра | Статус | Суть (что уникального) | Идея(и) статьи | Сайт |
|---|------|-------|------|------|--------|------------------------|----------------|------|
| 1 | VACnet (ML-половина VAC) | vacban wiki | 2018→ | CS2 | сниппет | «atom» на каждый выстрел: окно −0.5с/+0.25с, pitch/yaw+контекст; 140 атомов/8 раундов → скор | «Как VAC видит аимбот: разбор VACnet» | cheatsgaming.com |
| 2 | VAC Live (боевой слой) | vacban wiki | 2023→ | CS2 | сниппет | действует в матче: отмена/кулдаун/бан; отмена ≠ перманентный бан | «VAC Live: почему матч отменили, а бана нет» | cheatsgaming.com |
| 3 | VAC Live ловит за раунды | Hexxi (UC) | 2025 | CS2 | сниппет | external без записи памяти ловится по HS%/килам сквозь дым-стены; closet пока ок | «Что реально палит VAC Live в 2025» | cheatsgaming.com |
| 4 | Факторы флага VAC Live | shakro/Menalix (UC) | 2025 | CS2 | сниппет | trust vector, фикс. input rate, прямая запись viewangles — флаги серверной стороны | «Trust factor и серверный детект CS2» | cheatsgaming.com |
| 5 | История VAC/VAC2 | Wikipedia | 2002→ | CS2/CSGO | сниппет | сигнатурный скан→perma-баны (2005)→VACnet→VAC Live | «20 лет VAC: эволюция анти-чита Valve» | cheatsgaming.com |
| 6 | Vanguard dispatch-hooks | Archie | 2025 | Valorant | сниппет | хуки в .data вне PatchGuard; SwapContext-бит; HalCollectPmcCounters | «Почему Vanguard — эталон kernel-AC» | cheatsgaming.com |
| 7 | Vanguard IAT-hook vgk.sys | gmh5225 | n/a | Valorant | сниппет | хук IAT драйверов на MmCopyVirtualMemory, не inline → не триггерит PatchGuard | (в составе обзора Vanguard) | cheatsgaming.com |
| 8 | Vanguard page-fault детект | 0avx | n/a | Valorant | сниппет | execute-disable на PTE → #PF → KiPageFault логирует manual-map | «Как ловят manually-mapped драйверы» | cheatsgaming.com |
| 9 | VanguardTrace (enc imports) | armvirus | 2024 | Valorant | сниппет | расшифровка/перехват зашифрованных импортов vgk.sys | (тех. врезка) | cheatsgaming.com |
| 10 | Valorant Guarded Regions | Xyrem | n/a | Valorant | сниппет | shadow PML4/смена таблиц страниц — память игры невидима чужим | «Shadow page tables: как прячут память игры» | cheatsgaming.com |
| 11 | EAC/EOS драйвер | goldzik1/life45/UC | 2025 | multi | сниппет | колбэки process/thread/image/NMI; VM-защита логики; MSR/hypervisor-пробы | «Как устроен Easy Anti-Cheat» | cheatsgaming.com |
| 12 | BattlEye BEClient | secret.club/UC | 2019-25 | multi | сниппет | Init под VMP; AES-128, 60с цикл, LCG PRNG; денилист драйверов по timestamp | «BattlEye изнутри» | cheatsgaming.com |
| 13 | FACEIT AC + HWID | UC/arxiv | n/a | CS2 | сниппет | boot-driver, TPM/SecureBoot/DEP; HWID = серийник диска + MAC | «Почему FACEIT ловит то, что VAC не ловит» | cheatsgaming.com |
| 14 | Kernel-AC overview | Tulach/s4dbrd | n/a | multi | сниппет | big-pool скан, NMI-стек, целостность образа — детект manual-map | «Как работают kernel-античиты» | cheatsgaming.com |
| 15 | Deadlock интегрити-чеки | UC 729952 | 2024 | Deadlock | прочитано | citadel.signatures (SHA1/CRC32); детур NtOpenFile/LoadLibraryExW/PeekMessageW без -insecure | «Встроенный анти-чит Deadlock: что он проверяет» | deadlockhacks.com |
| 16 | Deadlock: VAC отключён | UC 745313 | 2025 | Deadlock | сниппет | активны только DLL/vtable проверки; manual-map обходит PEB | «Насколько безопасны читы в Deadlock сейчас» | deadlockhacks.com |
| 17 | Deadlock диагностика protobuf | ianveig29 | n/a | Deadlock | сниппет | CUserMessage_DllStatus: список модулей/подписи/HWID по сети | (врезка) | deadlockhacks.com |
| 18 | Trust Factor | Valve blog | n/a | CS2 | сниппет | скрытый аккаунт-скор; активность в др. Steam-играх; веса не раскрыты | «Trust Factor: что известно и что нет» | cheatsgaming.com |
| 19 | Волны банов CS2 2024 | dotesports/vacban | 2024 | CS2 | сниппет | 27.04.2024 ~130 VAC+64 game; май — десятки/сотни тыс.; трекер vac-ban | «Хронология VAC-банволн CS2» | cheatsgaming.com |
| 20 | Source2 schema system | VRF/GAMMACASE | n/a | Source2 | сниппет | рантайм-раскладки классов через schemasystem.dll вместо netvars | «Почему в Source 2 нет netvars» | melonity.gg |
| 21 | Source2Gen SDK-ген | neverlosecc | n/a | CS2/Dota2/Deadlock | сниппет | авто-SDK из бинаря игры для 3 игр | (тех. врезка для чит-дев) | cheatsgaming.com |
| 22 | cs2-universal-offsets | scros22 | n/a | CS2 | сниппет | живой дамп offset/vtable/netvars из cs2.exe | — | cluster.center |
| 23 | CS2 entity-list traversal | UC 734730 | 2026-01 | CS2 | сниппет | формула chunk/stride; controller→pawn; stride 0x78→0x70 | «Как читы находят игроков в CS2» | cluster.center |
| 24 | CS2 skin changer | UC 738534/github | n/a | CS2 | сниппет | EconItemView: paint6/seed7/wear8, MeshGroupMask, регенерация | «Как работает skin changer в CS2» | metaskins.gg |
| 25 | CS2 DMA радар + fuser | chao-shushu/UC | n/a | CS2 | сниппет | второй ПК читает память по PCIe, fuser сводит видео | «DMA-читы: почему их трудно поймать» | cluster.center |
| 26 | Aimbot humanizer | UC/intellisec | 2020→ | multi | сниппет | детект по последовательности углов, не по гладкости; рандомизация шагов | «Humanizer: что это и почему он важен» | melonity.gg |
| 27 | Triggerbot и детект | github/UC | n/a | CS2 | сниппет | детект по времени spotted→выстрел; задержка ~130мс | «Триггербот: механика и риски» | cluster.center |
| 28 | Deadlock auto-parry | UC 739608 | n/a | Deadlock | сниппет | хук GE_SosStartSoundEvent, проверка charge/дист/видимости | «Auto-parry в Deadlock: как устроено» | deadlockhacks.com |
| 29 | Dota 2 open-source читы | gmh5225/LWSS/UC | n/a | Dota2 | сниппет | динамич. schema, хук overlay, Panorama/protobuf | «История читов на Dota 2» | melonity.gg / dota2cheat.com |
| 30 | internal vs external | сводно (UC) | n/a | CS2 | сниппет | internal палевнее, external без записи дольше живёт, DMA ещё безопаснее | «Internal vs External vs DMA» | cheatsgaming.com |
| 31 | colby57: SCP:SL AC | colby57 | 2022-08 | SCP:SL | прочитано | 19-стр. PDF-разбор анти-чита SCP:SL (Themida) | — | cheatsgaming.com |
| 32 | colby57: Denuvo | colby57 | 2023-12 | multi | сниппет | хеширование KUSER_SHARED_DATA/PEB, связка со Steam DRM | «Denuvo простыми словами» | cheatsgaming.com |
| 33 | colby57: Legendware V5 | colby57 | 2025-05 | CS2 | сниппет | лоадер: ~60 мап-регионов, PEB/hypervisor/CPUID чеки | «Как устроены лоадеры читов» | cheatsgaming.com |
| 34 | colby57: Overwatch 2 RE | colby57 | 2023-24 | OW2 | сниппет | деобфускация импортов, исключения/ремаппинг/анти-дебаг | — | cheatsgaming.com |
| 35 | colby57: VMP деобфускатор | colby57 | 2024-25 | n/a | сниппет | vid/VMP-Imports-Deobfuscator: восстановление IAT VMProtect | «VMProtect: как защищают читы» | cheatsgaming.com |
| 36 | colby57: sec_no_syscalls | colby57 | 2024 | n/a | сниппет | прямые syscalls в обход user-mode хуков | (тех. врезка) | cheatsgaming.com |
| 37 | colby57: instrumentation cb | colby57 | 2025 | n/a | сниппет | Process Instrumentation Callback — перехват kernel→user | — | cheatsgaming.com |
| 38 | colby57: разборы лоадеров | colby57 | 2021-22 | CSGO | сниппет | AIMWARE/Neverlose/Onetap/Interium/Midnight — анти-дебаг трюки | «Эволюция лоадеров читов» | cheatsgaming.com |
| 39 | colby57: вирусы под кряки | colby57 | 2024 | CSGO/CS2 | сниппет | реверс «вирусов» под видом кряков читов (30k просмотров) | «Скам на рынке читов» | cheatsgaming.com / melonity.gg |
| 40 | colby57: Milfuscator/SpirtHack | colby57 Boosty | n/a | CS:GO/CS2 | сниппет | разработчик обфускатора и защиты чит-проекта | «Кто и как защищает читы» | cheatsgaming.com |
| 41 | Overwatch (ручной ревью) | dotesports/Valve | 2024 | CS2 | сниппет | вернули 25-26.04.2024; смотрят аим/vision/внешнюю помощь | «Overwatch vs VAC: в чём разница» | cheatsgaming.com |
| 42 | CS2 server-side ML AC (сторонний) | Driw0x/CS2Guard | n/a | CS2 | сниппет | демо-анализ + сдвигающиеся окна фич, скор подозрительности | «Можно ли ловить читеров без kernel» | cheatsgaming.com |

## Топ-10 идей для статей
1. «Как VAC видит аимбот»: разбор VACnet (atoms, окно вокруг выстрела) и VAC Live. — cheatsgaming.com
2. «VAC Live отменил матч, а бана нет»: механика отмена+кулдаун vs перманентный бан. — cheatsgaming.com
3. «Встроенный анти-чит Deadlock»: citadel.signatures + детуры NtOpenFile/LoadLibraryExW/PeekMessageW. — deadlockhacks.com
4. «Почему в Source 2 нет netvars»: schema system и как читы берут раскладки классов. — melonity.gg
5. «DMA-читы»: второй ПК + fuser, почему их тяжело детектить, где всё равно палятся. — cluster.center
6. «Humanizer в аимботе»: почему кривые Безью не спасают, что реально снижает детект. — melonity.gg
7. «20 лет VAC»: сигнатуры → VAC2 → VACnet → VAC Live, с датами банволн CS2 2024. — cheatsgaming.com
8. «Как работают kernel-античиты» (Vanguard/EAC/BattlEye/FACEIT) и чем VAC от них отличается. — cheatsgaming.com
9. «Как устроены лоадеры приватных читов» по разборам colby57 (мапинг, анти-дебаг, PEB/hypervisor-чеки). — cheatsgaming.com
10. «Как работает skin changer в CS2»: EconItemView, paint/seed/wear, регенерация визуала. — metaskins.gg

## Не удалось открыть целиком (нужен браузер/логин — только сниппеты)
- Все треды **yougame.biz** (Cloudflare 429 на curl; страница тегов colby57 открылась через WebFetch):
  https://yougame.biz/threads/309741/ (Denuvo), https://yougame.biz/threads/351391/ (Legendware V5),
  https://yougame.biz/threads/300963/ (OW2 импорты), https://yougame.biz/members/314097/.
- Большинство тредов **unknowncheats.me** — только сниппеты поиска (curl по части URL висит/таймаутит;
  открылись целиком только UC 510652 и UC 729952). Ключевые для дочитки:
  708645 (VAC Live за раунды), 750674 (факторы флага), 749306 (EAC startup), 736294 (BattlEye EFT),
  258402 (FACEIT HWID), 734730 (entity traversal+оффсеты), 738534 (skin changer source),
  692217 (DMA radar), 739608 (auto-parry), 745313 (Deadlock AC статус), 373232 (Безье-аимбот).
- **boosty.to/colby57** — платный контент (PDF-статьи), виден только анонс.

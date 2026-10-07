# Устройство читов и реверс Source 2 (фактура для статей)

> Пересказ своими словами; без пошаговых инструкций. Каждый пункт — с URL. «сниппет» = только сниппет.

## Source 2: схемы, offset'ы, entity system (CS2 / Dota 2 / Deadlock)
- **Schema system** — в Source 2 полные раскладки классов доступны в рантайме через schemasystem.dll,
  поэтому вместо «netvars» в стиле Source 1 используют schema-dumper'ы.
- **DumpSource2** (ValveResourceFormat) — офлайн-дамп schema-биндингов, convar'ов, команд из файлов игры.
  https://github.com/valveresourceformat/dumpsource2/ — **сниппет**
- **Source2SchemaDumper** (GAMMACASE) — Metamod-плагин, дампит схемы CS2 в JSON/KV3 (метатеги, atomics,
  pulse-биндинги, netvar-оверрайды). https://github.com/GAMMACASE/Source2SchemaDumper — **сниппет**
- **cs2-universal-offsets** (scros22) — живой external-дамп из cs2.exe: schema-хедеры, offset'ы,
  интерфейсы, vtables, netvars. https://github.com/scros22/cs2-universal-offsets — **сниппет**
- **Source2Gen / source2sdk** (neverlosecc) — генератор SDK для Source 2, поддержка CS2/Dota2/Deadlock
  (`conan build -o "game=DEADLOCK"`), выдаёт C++23/C23/IDA-хедеры. https://github.com/neverlosecc/source2gen — **сниппет**
- **Entity-list traversal (CS2)** — EntityList в client.dll; для id: chunk = EntityList + 8*(id>>9) + 0x10,
  затем entity = chunk + stride*(id & 0x1FF); контроллер → m_hPlayerPawn → снова через список к
  C_CSPlayerPawn. Актуальные оффсеты (янв 2026, из темы UC): dwEntityList 0x1D13CE8, dwViewMatrix
  0x1E323D0, m_hPlayerPawn 0x7E4, m_iHealth 0x34C; stride сменился 0x78→0x70. (Оффсеты протухают после
  апдейтов — ценность в механике, не в числах.) https://www.unknowncheats.me/.../734730-...traversal-issue.html — **сниппет**
- Образцы internal-читов CS2 (учебные): https://github.com/MitilcC/CS2-Internal-Cheat — **сниппет**

## ESP / Aimbot / Triggerbot
- **ESP** строится на entity-list + ViewMatrix (world→screen); health/team/pos из schema-полей.
- **Aimbot humanizer** — «безопасность» не в кривых Безье самих по себе: детекторы смотрят на
  последовательности углов и события выстрела, а не на гладкость. Подход «менее палевно»: дробить
  доворот на много мелких шагов, добавлять пошаговый шум, варьировать тайминг/скорость, точно сохранять
  конечную цель; избегать идеального аима/recoil и стабильно высокого перформанса. UC-тред по Безье +
  академ. работа «Aim Low, Shoot High». https://www.unknowncheats.me/forum/counterstrike-global-offensive/373232-bezier-curves-mouse_events-aimbot.html ·
  https://intellisec.de/research/aimbots/2020-eurosec.pdf — **сниппет**
- **Triggerbot & детект** — ловится по времени между «цель видима/spotted» и первым выстрелом; стабильно
  около-нулевая реакция подозрительна (но pre-fire/пинг дают ложные срабатывания). Сервер может
  использовать spotted/LOS-состояние CS2. Совет из UC: держать задержку триггера ~130мс. 
  https://github.com/killerbigpoint/cs2-anticheat/issues/45 — **сниппет**

## Skin changer (CS2) — механика
- Модификация C_EconItemView оружия: запись fallback paint kit, seed, wear, item id, затем принудительная
  пересборка визуала. Для external также правят MeshGroupMask у weapon/viewmodel scene-node (1 modern /
  2 legacy), вызывают UpdateSubClass/SetModel или регенерацию. Атрибуты: paint = 6, pattern/seed = 7,
  wear = 8 в AttributeList; internal может задавать через C_EconItemView::SetAttributeValueByName.
  https://www.unknowncheats.me/forum/counter-strike-2-releases/738534-cs2-external-skin-changer-source.html ·
  https://github.com/madiskoivopuu/cs2skinchangermenu — **сниппет**

## DMA-читы и радары (hardware)
- FPGA/PCIe DMA-устройство на втором ПК читает память игрового ПК (read-only, игра работает штатно),
  парсит entity-позиции/HP/team/map по актуальным оффсетам, рисует ESP/радар на втором ПК; **fuser**
  сводит видеосигнал второго ПК и игрового в один монитор. Клиент батчит разрозненные чтения, кэширует
  низкочастотные поля, публикует снапшоты для рендера/WebSocket-радара. https://github.com/chao-shushu/CS2-DMA ·
  https://www.unknowncheats.me/forum/counter-strike-2-a/692217-cs2-dma-board-radar.html — **сниппет**

## Deadlock — auto-parry
- Хук сетевых sound-событий (GE_SosStartSoundEvent, парсинг engine2.dll), определение charge ближней
  атаки врага, проверка дистанции/видимости/направления и готовности способности → автопарирование.
  https://www.unknowncheats.me/forum/deadlock/739608-autoparry-issues.html — **сниппет**

## Dota 2 — реверс и open-source читы (история/механика)
- gmh5225/dota-cheat (native C++, динамические schema-оффсеты, хук GameOverlayRenderer);
  LWSS/McDota (Linux, Panorama UI, перехват protobuf, ESP, Cartographer); UC Dota 2 wiki.
  https://github.com/gmh5225/dota-cheat · https://github.com/LWSS/McDota · https://www.unknowncheats.me/wiki/Dota_2 — **сниппет**

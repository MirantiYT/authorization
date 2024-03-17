pyinstaller --onefile ^
  --add-data "sec.png;." ^
  --add-data "vk.jpg;." ^
  --add-data "zak.jpg;." ^
  --add-data "zamok.png;." ^
  --log-level=DEBUG ^
  --noconsole ^
  authorization.py

pause
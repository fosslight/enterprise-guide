from pathlib import Path
import shutil


enterprise_root = Path(__file__).resolve().parent.parent

# GitHub Actions에서 사용하는 위치
external_hub = enterprise_root / "_external" / "hub-guide"

# 로컬에서 사용하는 위치
sibling_hub = enterprise_root.parent / "hub-guide"

external_document = external_hub / "menu" / "9_system.md"
sibling_document = sibling_hub / "menu" / "9_system.md"

# 폴더가 아니라 실제 파일이 있는지 확인합니다.
if external_document.is_file():
    hub_root = external_hub
elif sibling_document.is_file():
    hub_root = sibling_hub
else:
    raise FileNotFoundError(
        "Hub Guide의 menu/9_system.md를 찾을 수 없습니다.\n"
        f"확인한 위치:\n"
        f"- {external_document}\n"
        f"- {sibling_document}"
    )

hub_document = hub_root / "menu" / "9_system.md"
hub_image = hub_root / "menu" / "images" / "9_system_mail.png"

target_document = (
    enterprise_root
    / "hub"
    / "guide"
    / "manager"
    / "user_management"
    / "sent_mail_list.md"
)

target_image = (
    enterprise_root
    / "hub"
    / "guide"
    / "manager"
    / "user_management"
    / "images"
    / "9_system_mail.png"
)


if not hub_document.exists():
    raise FileNotFoundError(
        f"Hub Guide 문서를 찾을 수 없습니다: {hub_document}"
    )

lines = hub_document.read_text(encoding="utf-8").splitlines(
    keepends=True
)

start_index = None

for index, line in enumerate(lines):
    if line.strip() == "## Sent Mail List":
        start_index = index
        break

if start_index is None:
    raise RuntimeError(
        "9_system.md에서 Sent Mail List를 찾을 수 없습니다."
    )

end_index = len(lines)

for index in range(start_index + 1, len(lines)):
    if lines[index].startswith("## "):
        end_index = index
        break

section = "".join(lines[start_index:end_index]).rstrip()

front_matter = """---
title: Sent Mail List
sort: 2
published: true
---
"""

target_document.parent.mkdir(parents=True, exist_ok=True)

target_document.write_text(
    f"{front_matter}\n{section}\n",
    encoding="utf-8",
)

if not hub_image.exists():
    raise FileNotFoundError(
        f"Hub Guide 이미지를 찾을 수 없습니다: {hub_image}"
    )

target_image.parent.mkdir(parents=True, exist_ok=True)
shutil.copy2(hub_image, target_image)

print("Sent Mail List 동기화가 완료되었습니다.")

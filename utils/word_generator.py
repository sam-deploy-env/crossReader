import xml.etree.ElementTree as ET
import zipfile
import shutil
import os

from utils import rewards
from constants import file_data

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"

def create_word_file(category_repo, runner_repo):
    old_text_list = []
    new_text_list = []
    rewards_to_display = rewards.get_rewards_to_display(category_repo, runner_repo)
    for reward in rewards_to_display:
        if reward.ranking is None:
            continue
        distance = reward.race_label.split("k")[0]
        sex = reward.sex if reward.sex != "M" else "H"
        old_text_list.append("R" + reward.category + sex + distance)
        new_text_list.append(str(reward.ranking))
        old_text_list.append("L" + reward.category + sex + distance)
        new_text_list.append(reward.last_name)
        old_text_list.append("F" + reward.category + sex + distance)
        new_text_list.append(reward.first_name)
        old_text_list.append("T" + reward.category + sex + distance)
        new_text_list.append(reward.time)
    replace_text_in_document(old_text_list, new_text_list)

def replace_text_in_document(old_text_list, new_text_list):
    unzip_docx(file_data.EMPTY_WORD_FILENAME, file_data.TEMP_FILENAME)
    xml_file_path = os.path.join(file_data.TEMP_FILENAME, 'word/document.xml')
    for old, new in zip(old_text_list, new_text_list):
        replace_flag_in_xml(xml_file_path, old, new)
    zip_dir(file_data.TEMP_FILENAME, file_data.FINAL_WORD_FILENAME)
    shutil.rmtree(file_data.TEMP_FILENAME)

def unzip_docx(docx_path, extract_to):
    with zipfile.ZipFile(docx_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def zip_dir(directory, zip_file):
    with zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                arc_name = os.path.relpath(file_path, directory)
                zipf.write(file_path, arc_name)

def replace_flag_in_xml(file_path, flag, value):
    tree = ET.parse(file_path)
    root = tree.getroot()

    for paragraph in root.iter(f"{{{W_NS}}}p"):
        text_elements = list(paragraph.iter(f"{{{W_NS}}}t"))

        # Texte complet du paragraphe
        full_text = "".join(
            elem.text or "" for elem in text_elements
        )

        if flag not in full_text:
            continue

        new_text = full_text.replace(
            flag,
            value if value is not None else ""
        )

        # On met le texte complet dans le premier élément
        if text_elements:
            text_elements[0].text = new_text

            # On vide les autres éléments
            for elem in text_elements[1:]:
                elem.text = ""

    tree.write(
        file_path,
        encoding="UTF-8",
        xml_declaration=True
    )

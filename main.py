from gtts import gTTS
import pdfplumber
from pathlib import Path


def pdf_to_mp3(filepath='test.pdf', language='en'):
    if Path(filepath).is_file() and Path(filepath).suffix == '.pdf':
        print ('[+] Processing...')
        with pdfplumber.PDF(open(file=filepath, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]
            text = ''.join(pages)

        with open('text1.txt', 'w') as file:
            file.write(text)
            text = text.replace('\n','')
            my_audio = gTTS(text=text, lang=language, slow=False)
            file_name= Path(filepath).stem
            my_audio.save(f'{file_name}.mp3')
            return f'{file_name}.mp3 saved.'
    else:
        return 'Check the file path. Seems like it is wrong.'


def main():
    filepath= input("\nEnter file's path:")
    language = input("\nWhat is the language of file?\nEn/Ru?\n")
    print(pdf_to_mp3())


if __name__ == '__main__':
    main()
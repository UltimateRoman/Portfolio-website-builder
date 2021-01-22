from bs4 import BeautifulSoup

def main():
    with open("portfolio/index.html") as f1:
        inst = BeautifulSoup(f1, 'html.parser')
        tag1 = inst.title
        tag2 = inst.body.a
        ntag = inst.find('h2')
        for b in inst.find_all('h2'):
            if b['class'][0] == 'about__subtitle':
                btag = b
                break
        name = input("Enter your name: ")
        tag1.string.replace_with(name)
        tag2.string.replace_with(name)
        ntag.string.replace_with("I'm "+name+"!")
        btag.string.replace_with("I'm "+name)

        tline = input("Enter your tagline: ")
        for a in inst.find_all('span'):
            if a['class'][0] == 'about__profession':
                atag = a
                break 
        atag.string.replace_with(tline)

        for a in inst.find_all('p'):
            if a['class'][0] == 'about__text':
                atag = a
                break        
        about = input("Enter a brief description about yourselves: ")
        atag.string.replace_with(about)
        f1.close()
        
    with open("portfolio/index.html", "w") as f2:
        f2.write(str(inst))
        print("Your portfolio website has been generated in the /portfolio directory.")

if __name__ == '__main__':
    main()

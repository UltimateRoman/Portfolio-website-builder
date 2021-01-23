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

        link = input("Enter your linkedn link : ")
        for a in inst.find_all('a'):
            if a['class'][0] == 'about__social-icon1':
                atag = a
                break 
        atag['href'] = link

        git = input("Enter your github link : ")
        for a in inst.find_all('a'):
            if a['class'][0] == 'about__social-icon':
                atag = a
                break 
        atag['href'] = git

        email = input("Enter your professional use email: ")
        for a in inst.find_all('span'):
            if a['class'][0] == 'contact__text1':
                atag = a
                break 
        atag.string.replace_with(email)

        num = input("Enter your professional use phone number: ")
        for a in inst.find_all('span'):
            if a['class'][0] == 'contact__text2':
                atag = a
                break 
        atag.string.replace_with(num)
        
        con = input("Enter your country : ")
        for a in inst.find_all('span'):
            if a['class'][0] == 'contact__text3':
                atag = a
                break 
        atag.string.replace_with(con)

        a = input("Would you like to showcase your projects ? ")
        if a == 'yes':
            link = input("Enter your project's github repository link : ")
            for a in inst.find_all('a'):
                if a['class'][0] == 'portfolio__link-name1':
                    atag = a
                    break 
            atag['href'] = link
            b = input("Would you like to showcase another projects ? ")
            if b == 'yes':
                link = input("Enter your project's github repository link : ")
                for a in inst.find_all('a'):
                    if a['class'][0] == 'portfolio__link-name2':
                        atag = a
                        break 
                atag['href'] = link
                c = input("Would you like to showcase another projects ? ")
                if c == 'yes':
                    link = input("Enter your project's github repository link : ")
                    for a in inst.find_all('a'):
                        if a['class'][0] == 'portfolio__link-name':
                            atag = a
                            break 
                    atag['href'] = link

        f1.close()
        
    with open("portfolio/index.html", "w") as f2:
        f2.write(str(inst))
        print("Your portfolio website has been generated in the /portfolio directory.")

if __name__ == '__main__':
    main()

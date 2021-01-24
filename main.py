from bs4 import BeautifulSoup

def main():
    with open("portfolio/index.html") as f1:
        inst = BeautifulSoup(f1, 'html.parser')
        tag1 = inst.title
        tag2 = inst.body.a
        ntag = inst.find('h2')
        for a in inst.find_all('h2'):
            if a['class'][0] == 'footer__title':
                ntag2 = a
                break
        for b in inst.find_all('h2'):
            if b['class'][0] == 'about__subtitle':
                btag = b
                break
        for c in inst.find_all('p'):
            if c['class'][0] == 'footer__text':
                ctag = c
                break
        name = input("Enter your name: ")
        tag1.string.replace_with(name)
        tag2.string.replace_with(name)
        ntag2.string.replace_with(name)
        ntag.string.replace_with("I'm "+name+"!")
        btag.string.replace_with("I'm "+name)
        ctag.string.replace_with("I'm "+name+" and this is my portfolio website.")

        tline = input("Enter a tagline: ")
        for a in inst.find_all('span'):
            if a['class'][0] == 'about__profession':
                atag = a
                break 
        atag.string.replace_with(tline)

        for a in inst.find_all('p'):
            if a['class'][0] == 'about__text':
                atag = a
                break        
        about = input("Enter a brief description about yourself: ")
        atag.string.replace_with(about)

        link = input("\nPlease provide your Linkedn handle: ")
        for a in inst.find_all('a'):
            if a['class'][0] == 'about__social-icon1':
                atag = a
                break 
        atag['href'] = link

        git = input("Please enter your GitHub profile link: ")
        for a in inst.find_all('a'):
            if a['class'][0] == 'about__social-icon':
                atag = a
                break 
        atag['href'] = git

        print("\nPlease provide your contact details")
        email = input("Your professional use email: ")
        for a in inst.find_all('span'):
            if a['class'][0] == 'contact__text1':
                atag = a
                break 
        atag.string.replace_with(email)

        num = input("Your professional use phone number: ")
        for a in inst.find_all('span'):
            if a['class'][0] == 'contact__text2':
                atag = a
                break 
        atag.string.replace_with(num)
        
        con = input("Country : ")
        for a in inst.find_all('span'):
            if a['class'][0] == 'contact__text3':
                atag = a
                break 
        atag.string.replace_with(con)

        print("\nEnter your top 5 skills: ")
        for b in inst.find_all('span'):
            if b['class'][0] == 'skills__name':
                s = input()
                b.string.replace_with(s)

        a = input("\nWould you like to showcase some of your projects ? ")
        if a == 'yes':
            pname = input("Project name: ")
            link = input("Enter project1's link : ")
            for a in inst.find_all('a'):
                if a['class'][0] == 'portfolio__link-name1':
                    atag = a
                    break 
            atag.string.replace_with(pname)
            atag['href'] = link
            b = input("Would you like to showcase another project ? ")
            if b == 'yes':
                pname = input("Project name: ")
                link = input("Enter project2's link : ")
                for a in inst.find_all('a'):
                    if a['class'][0] == 'portfolio__link-name2':
                        atag = a
                        break
                atag.string.replace_with(pname) 
                atag['href'] = link
                c = input("Would you like to showcase one more project ? ")
                if c == 'yes':
                    pname = input("Project name: ")
                    link = input("Enter project3's link : ")
                    for a in inst.find_all('a'):
                        if a['class'][0] == 'portfolio__link-name':
                            atag = a
                            break
                    atag.string.replace_with(pname) 
                    atag['href'] = link

        f1.close()
        
    with open("portfolio/index.html", "w") as f2:
        f2.write(str(inst))
        print("\nCongrats! Your portfolio website has been generated in the /portfolio directory.")

if __name__ == '__main__':
    main()

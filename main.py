from bs4 import BeautifulSoup

def main():
    with open("portfolio/index.html") as f1:
        inst = BeautifulSoup(f1, 'html.parser')
        tag1 = inst.title
        
        f1.close()
        
    with open("portfolio/index.html", "w") as f2:
        f2.write(str(inst))
        print("Your portfolio website has been generated in the /portfolio directory.")

if __name__ == '__main__':
    main()

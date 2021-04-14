#!/usr/bin/python3
import sys

def main():
    try:
        layout = zineGuide(
            subpages        = sys.argv[1],
            subPerPage      = sys.argv[2],
            includesCovers  = sys.argv[3],
            fileExtension   = sys.argv[4]
        )
    except:
        layout = zineGuide(47, 2, False,'jpg')

    print(layout)



class zineGuide:
    # 1 Sheet of paper = 2 pages = 4 subpages
    def __init__(self,subpages, subPerPage = 2, includesCovers=True, fileExtension='jpg'):
        self.subpages = int(subpages)
        self.subPerPage = int(subPerPage)
        self.includesCovers = bool(includesCovers)
        self.fileExtension = str(fileExtension)
        print(">You requested:",self.subpages,"subpages,",self.subPerPage,"subpages per page")
        if not self.includesCovers: 
            # Insert 2 subpages to make room for Front and Back Cover
            print(">Inserting 2 subpages for front/back covers")
            self.subpages += 2
        if self.subpages % subPerPage > 0:
            inserts = self.subpages % subPerPage
            print(">Inserting",inserts,"additional subpages to fill last page")
            self.subpages += inserts

    @property
    def pages(self):
        initial = int(self.subpages / 2)
        additional = initial % 2
        return initial + additional

    @property
    def sheetArray(self):
        pages = [ [ [] for j in range(self.subPerPage) ] for i in range(self.pages) ]
        subPageCounterLeft = 0
        subPageCounterRight = len(pages)*2-1
        counter = 0
        for i in range(self.pages):
            for j in range(self.subPerPage):
                if counter % 2 == 0:
                    pages[i][j] = str(subPageCounterLeft).zfill(3)+'.'+self.fileExtension
                    subPageCounterLeft += 1
                else:
                    pages[i][j] = str(subPageCounterRight).zfill(3)+'.'+self.fileExtension
                    subPageCounterRight -= 1
                counter += 1
        return pages

    def __str__(self):
        #output = "halves:\t"+str(self.subpages)+"\npages:\t"+str(self.pages)+"\nsheets:\t"+str(self.sheets)
        output = ""
        pageCount = 1
        sheetCount = 0
        for sheet in self.sheetArray:
            if pageCount % 2 == 1:
                sheetCount += 1
            output += "S"+str(sheetCount).zfill(3)+"\tP"+str(pageCount).zfill(3)+":\t"
            output += str(sheet)
            output += '\n'
            pageCount += 1
        output += "> "+str(sheetCount)+" Sheets;"+str(self.pages)+" Pages;"+str(self.subpages)+" Subpages;"
        return output
    
if __name__ == '__main__':
    main()
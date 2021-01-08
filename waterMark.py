from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

packet = io.BytesIO()
# create a new PDF with Reportlab
can = canvas.Canvas(packet, pagesize=letter)
can.drawString(10, 100, 
''',_.                                                          ,_.
'\cXX.==- __                                        __ -==,XXv/`
    ~=_X7~ ,/~!g=-,_.                      ,_.-=s!~L. ~TX_=~
       ~=c. = /- T--e'T|=v._  ....   _,v=!7`z--\ -\ = ,v=~
          ~=c` ./ ,-`,/ /i/Z\/~~~~\/Z\i\ \.'-. \, 'v=~
             ~\s,/ ,/ ,/ Y]`/ @/\@ '[Y \. \. \.g/~
                '`Yc.v`,/Vs)-  \/  -(sV\.'c,v+'`
                     ~~]mZczTV '` VTevZm[~~
                  ,=-T|--2Y [      ] Y2--!T-=.
                  'i`_ -|-'i!      !i`-!- _'i`
                    '-s|.cf ,!]\/[!. 1v,!g-`
                        ~Y/v/vv..vv♂\Y~
                         ^            ^
''')
can.save()

#move to the beginning of the StringIO buffer
packet.seek(0)
new_pdf = PdfFileReader(packet)
# read your existing PDF
existing_pdf = PdfFileReader(open("test.pdf", "rb"))
output = PdfFileWriter()
# add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)
# finally, write "output" to a real file
outputStream = open("destination.pdf", "wb")
output.write(outputStream)
outputStream.close()
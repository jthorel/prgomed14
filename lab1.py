def paketPris(paketVikt):
    if paketVikt<2:
        return paketVikt*30
    elif paketVikt<6:
        return paketVikt*28
    elif paketVikt < 12:
        return paketVikt*25
    elif paketVikt >= 12:
        return paketVikt*23
      

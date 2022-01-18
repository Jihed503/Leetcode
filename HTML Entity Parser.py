class Solution:
    def entityParser(self, text: str) -> str:
        d={'&quot':'"','&apos':"'",'&amp':'&','&gt':'>','&lt':'<','&frasl':'/'}
        ch=text.replace('&quot;','"')
        ch=ch.replace('&apos;',"'")
        ch=ch.replace('&amp;','&')
        ch=ch.replace('&gt;','>')
        ch=ch.replace('&lt;','<')
        ch=ch.replace('&frasl;','/')
        return ch
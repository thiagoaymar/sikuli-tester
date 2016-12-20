salvar = "salvar.png"
chrome = "chrome.png"
wait(2)
type("1482254714184.png", "med.praxisapp.com.br" + Key.ENTER)
type("1482254739415.png", "teste@teste.com" + Key.TAB + "teste" + Key.ENTER)
click("1482255561016.png")
click(Pattern("1482255836071.png").targetOffset(91,-1))
wait("1482255873987.png")
click(Pattern("1482256036703.png").targetOffset(36,0))
type("Thiago Aymar" + Key.TAB + "12170170464" + Key.TAB + "81998229262")
click(Pattern("1482257877699.png").targetOffset(-76,-1))

type(Pattern("1482256492841.png").targetOffset(34,1),"21122016")
type(Pattern("1482256778916.png").targetOffset(22,-1),"1500")
type(Pattern("1482256579918.png").targetOffset(-7,25), "Teste concluido com sucesso!")
click(salvar)
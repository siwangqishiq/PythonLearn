#包导入 测试类
#import gameTool
from gameTool import game_lib , render

game_main = game_lib.MonsterMain()
game_main.main()

render = render.Render()
render.show()
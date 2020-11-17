import cx_Freeze

executables = [cx_Freeze.Executable("game.py")]

cx_Freeze.setup(
	name="Snakes@Ev|L",
	options={"build_exe":{"packages":["pygame"], "include_files":["bgimg.jpg", "gameover.jpg", "highscore.txt", "IMP readme.txt", "Untitled.jpg", "intro.mp3", "ingamebg.mp3", "gameover.mp3", "eat.mp3", ""]}},
	version="1.0",
	executables=executables
	)
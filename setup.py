import cx_Freeze
executables = [cx_Freeze.Executable(
    script="snake.py", icon="assets/icon_game.ico")]

cx_Freeze.setup(
    name="Snake Educacional",
    options={
        "build_exe": {
            "packages": ["pygame"],
            "include_files": ["assets"]
        }},
    executables=executables
)

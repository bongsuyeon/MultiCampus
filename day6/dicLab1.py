color_info = {'red': '#ff0000',
             'blue': '#0066ff',
             'green': '#33cc33',
             'yellow': '#ffff00',
             'orange': '#ff9900',
             'black': '#000000',
             'white': '#ffffff',
             'violet': '#9900ff',
             'pink': '#ff00ff',
             'lime': '#ccffcc'}

key = input("칼라명을 영문으로 입력하세요 :")
if key in color_info:
    print(key, "칼라의 RGB 값은",color_info[key], "입니다")
else:
    print(key, "칼라의 RGB 값을 찾을 수 없습니다")

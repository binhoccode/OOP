def print_beam():
    print('+ - - - - + - - - - +')
def print_post():
    print('|         |         |')
    def print_four_posts():
        print_post()
        print_post()
        print_post()
        print_post()
    def draw_grid():
        print_beam()
        print_four_posts()
        print_beam()
        print_four_posts()
        print_beam()
    print("---- 2x2 Grid ----")
    draw_grid()
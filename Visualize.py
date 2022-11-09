import math
import random

from Algorithms import *
from DrawInfo import *


def generate_list(minimum=0, maximum=100, n=50):
    """Generates an array with given (or default)"""
    return [random.randint(minimum, maximum) for _ in range(n)]


def main():
    run = True
    clock = pygame.time.Clock()
    elements_in_array = 80

    lst = generate_list(n=elements_in_array)
    draw_info = DrawInfo(800, 600, lst)

    algo_name = "Bubble Sort"
    sorting_algorithm = bubble_sort
    sorting_algo_gen = None

    sorting = False
    ascending = True

    while run:
        clock.tick(60)

        # keeps advancing to the next step after each yield from the sorting generator.
        if sorting:
            try:
                next(sorting_algo_gen)
            except StopIteration:
                sorting = False
            except TypeError:
                sorting = False
        else:
            # if not sorting, drawing the screen.
            draw(draw_info, algo_name, ascending)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            if event.type != pygame.KEYDOWN:
                continue

            # Onclick R - generates new array.
            if event.key == pygame.K_r:
                lst = generate_list(n=elements_in_array)
                draw_info.set_list(lst)
                sorting = False

            # Onclick space and not sorting - starts to sort the array.
            elif event.key == pygame.K_SPACE and sorting is False:
                sorting = True
                if sorting_algorithm is quick_sort or sorting_algorithm is merge_sort:
                    sorting_algo_gen = sorting_algorithm(lst, draw_info, 0, len(lst) - 1, ascending)
                else:
                    sorting_algo_gen = sorting_algorithm(lst, draw_info, ascending)

            # changing sorting algorithms buttons
            elif event.key == pygame.K_b:
                sorting_algorithm = bubble_sort
                algo_name = "Bubble Sort"

            elif event.key == pygame.K_i:
                sorting_algorithm = insertion_sort
                algo_name = "Insertion Sort"

            elif event.key == pygame.K_m:
                sorting_algorithm = merge_sort
                algo_name = "Merge Sort"

            elif event.key == pygame.K_q:
                sorting_algorithm = quick_sort
                algo_name = "Quick Sort"

            # changing ascending or descending
            elif event.key == pygame.K_a and not sorting:
                ascending = True

            elif event.key == pygame.K_d and not sorting:
                ascending = False

    pygame.quit()


if __name__ == "__main__":
    main()


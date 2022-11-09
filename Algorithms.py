from drawing_methods import *


def bubble_sort(arr, draw_info, ascending=True):
    """Bubble Sort function."""

    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] < arr[j] and ascending or arr[i] > arr[j] and not ascending:
                arr[i], arr[j] = arr[j], arr[i]
                draw_list(draw_info, {j: draw_info.GREEN, i: draw_info.RED}, True)
                yield True


def insertion_sort(arr, draw_info, ascending=True):
    """Insertion Sort function."""

    for i in range(1, len(arr)):

        index = i - 1
        val = arr[i]

        while (index >= 0 and arr[index] > val and ascending) or (index >= 0 and arr[index] < val and not ascending):
            arr[index + 1] = arr[index]
            draw_list(draw_info, {i: draw_info.GREEN, index: draw_info.RED}, True)
            yield True

            index -= 1

        arr[index + 1] = val


def merge_sort(arr, draw_info, low, high, ascending=True):
    """Merge Sort function."""

    if low >= high:
        return

    mid = low + (high - low) // 2

    yield from merge_sort(arr, draw_info, low, mid, ascending)
    yield from merge_sort(arr, draw_info, mid+1, high, ascending)

    yield from merge(arr, draw_info, low, high, mid, ascending)
    yield True


def merge(arr, draw_info, l, r, mid, ascending):

    """helper function for merge_sort,
    merges two SORTED sections of the array into one SORTED array.
    """

    left_length = mid - l + 1
    right_length = r - mid

    right_half = [arr[mid + i + 1] for i in range(0, right_length)]
    left_half = [arr[l + i] for i in range(0, left_length)]

    i = j = 0
    k = l

    while i < left_length and j < right_length:
        if left_half[i] < right_half[j] and ascending or left_half[i] > right_half[j] and not ascending:
            arr[k] = left_half[i]
            draw_list(draw_info, {i: draw_info.GREEN, k: draw_info.RED}, True)
            yield True

            i += 1

        else:
            arr[k] = right_half[j]
            draw_list(draw_info, {j: draw_info.GREEN, k: draw_info.RED}, True)
            yield True

            j += 1

        k += 1

    while i < left_length:
        arr[k] = left_half[i]
        draw_list(draw_info, {i: draw_info.GREEN, k: draw_info.RED}, True)
        yield True

        i += 1
        k += 1

    while j < right_length:
        arr[k] = right_half[j]

        draw_list(draw_info, {j: draw_info.GREEN, k: draw_info.RED}, True)
        yield True

        j += 1
        k += 1

    yield True


def quick_sort(arr, draw_info,  low, high, ascending=True):
    """Quick Sort function."""
    if low >= high:
        return

    pivot = arr[high]
    i = low - 1

    # finds proper spot for the pivot
    for j in range(low, high):
        if (arr[j] <= pivot and ascending) or (arr[j] >= pivot and not ascending):
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
            draw_list(draw_info, {i: draw_info.GREEN, j: draw_info.RED}, True)
        yield True

    # inserts pivot to proper place
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    draw_list(draw_info, {i: draw_info.GREEN, j: draw_info.RED}, True)
    yield True

    # sends left and right side of the pivot to be sorted too.
    pi = i + 1
    yield from quick_sort(arr, draw_info, low, pi - 1, ascending)
    yield from quick_sort(arr, draw_info, pi + 1, high, ascending)



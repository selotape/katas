from enum import Enum


class From(Enum):
    OLD = 'OLD'
    NEW = 'NEW'
    BOTH = 'BOTH'


class Segment:
    def __init__(self, source, text):
        self.source = source
        self.text = text

    def __str__(self):
        if self.source == From.BOTH:
            return self.text
        if self.source == From.OLD:
            return '({})'.format(self.text)
        if self.source == From.NEW:
            return '[{}]'.format(self.text)


def display_length(display_diff):
    return sum(len(segment.text) for segment in display_diff)


def displayDiff(old_version, new_version):
    mem = {}
    display_diff = best_display_diff(old_version, new_version, mem)
    return format_display(display_diff)


def best_display_diff(old_version, new_version, mem):
    mem_key = old_version, new_version
    if mem_key in mem:
        return mem[mem_key]

    if not old_version and not new_version:
        return []
    if not old_version:
        return [Segment(source=From.NEW, text=new_version)]
    if not new_version:
        return [Segment(source=From.OLD, text=old_version)]

    if old_version[0] == new_version[0]:
        both_future = best_display_diff(old_version[1:], new_version[1:], mem)
        best_future = merge_segment_with_future(Segment(source=From.BOTH, text=new_version[0]), both_future)
    else:
        old_first_future = best_display_diff(old_version[1:], new_version, mem)
        best_old_first_future = merge_segment_with_future(Segment(source=From.OLD, text=old_version[0]), old_first_future)

        new_first_future = best_display_diff(old_version, new_version[1:], mem)
        best_new_first_future = merge_segment_with_future(Segment(source=From.NEW, text=new_version[0]), new_first_future)

        if display_length(best_old_first_future) <= display_length(best_new_first_future):
            best_future = best_old_first_future
        else:
            best_future = best_new_first_future
    mem[mem_key] = best_future
    return best_future


def merge_segment_with_future(current_segment, future):
    if not future:
        return [current_segment]
    if future[0].source == current_segment.source:
        return [Segment(source=future[0].source, text=current_segment.text + future[0].text)] + future[1:]
    return [current_segment] + future


def format_display(display_diff):
    return ''.join(str(segment) for segment in display_diff)

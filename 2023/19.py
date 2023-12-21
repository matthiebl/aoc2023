#!/usr/bin/env python3.12

import aocutils as u
from sys import argv

Workflows = dict[str, tuple[list[tuple[str, str, int, str]], str]]

INDEX = {'x': 0, 'm': 1, 'a': 2, 's': 3}


def is_accepted(workflows: Workflows, name, ratings):
    if name == 'A':
        return True
    if name == 'R':
        return False
    rules, default = workflows[name]
    for (key, cmp, n, target) in rules:
        if cmp == '>' and ratings[INDEX[key]] > n:
            return is_accepted(workflows, target, ratings)
        if cmp == '<' and ratings[INDEX[key]] < n:
            return is_accepted(workflows, target, ratings)
    return is_accepted(workflows, default, ratings)


PREV = {}


def intersection(xmas, kind):
    not_checked = list(PREV.keys())
    splits = [xmas]
    while splits:
        this = splits.pop()
        intersections = False
        for prev in not_checked:
            # prev = not_checked.pop()
            ranges = [u.range_overlap(r1, r2) for r1, r2 in zip(this, prev)]
            inter = [b for _, b, _ in ranges]
            if any(a is None for a in inter):
                # no intersection
                continue
            intersections = True
            for a in ranges[0]:
                if a is None:
                    continue
                for b in ranges[1]:
                    if b is None:
                        continue
                    for c in ranges[2]:
                        if c is None:
                            continue
                        for d in ranges[3]:
                            if d is None:
                                continue
                            if [a, b, c, d] == inter:
                                continue
                            splits.append([a, b, c, d])
            break
        if not intersections:
            PREV[tuple(this)] = kind


def send(workflows, name, xmas):
    if any(b - a <= 0 for a, b in xmas):
        return
    if name == 'R' or name == 'A':
        intersection(xmas, name)
        return
    rules, default = workflows[name]
    xxmas = xmas.copy()

    for (key, cmp, n, target) in rules:
        index = INDEX[key]
        lo, hi = xxmas[index]
        xxxmas = xxmas.copy()
        if cmp == '>':
            xxxmas[index] = (max(lo, n + 1), hi)
            send(workflows, target, xxxmas)
            xxmas[index] = (lo, min(hi, n + 1))
        elif cmp == '<':
            xxxmas[index] = (lo, min(hi, n))
            send(workflows, target, xxxmas)
            xxmas[index] = (max(lo, n), hi)
    send(workflows, default, xxmas)


def main(file: str) -> None:
    print('Day 19')

    [instructions, parts] = u.input_from_grouped_lines(file)

    workflows: Workflows = {}
    for instruction in instructions:
        name, rules = instruction[:-1].split('{')
        rules = rules.split(',')
        workflows[name] = ([], rules.pop())
        for rule in rules:
            comparison, target = rule.split(':')
            key, cmp = comparison[0], comparison[1]
            n = int(comparison[2:])
            workflows[name][0].append((key, cmp, n, target))

    p1 = 0
    for coord in parts:
        nums = u.find_digits(coord)
        if is_accepted(workflows, 'in', nums):
            p1 += sum(nums)
    print(f'{p1=}')

    send(workflows, 'in', [(1, 4001), (1, 4001), (1, 4001), (1, 4001)])
    p2 = 0
    for l in PREV:
        if PREV[l] == 'A':
            p2 += u.mul(b - a for a, b in l)
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '19.in'
    main(file)

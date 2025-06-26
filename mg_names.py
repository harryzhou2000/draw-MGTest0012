import re


def parse_dnds_pmgs_name(name: str, default_len=0):
    subnames = name.split("-")
    base_name = subnames[0]
    seq_names = subnames[1:]
    seq_info = []
    for n in seq_names:
        match = re.match(r"(\d+)(.+)", n)
        if match is None:
            raise ValueError(f"'{n}' does not match a mg level name")
        seq_info.append((int(match.group(1)), match.group(2)))
    seq_info = [(1, base_name)] + seq_info
    if default_len > len(seq_info):
        seq_info = seq_info + [(0, None) for _ in range(default_len - len(seq_info))]
    return seq_info


if __name__ == "__main__":
    from pprint import pprint

    pprint(parse_dnds_pmgs_name("gmres5x1ilu-1ilu-4ilu"))
    try:
        parse_dnds_pmgs_name("gmres5x1ilu-1ilu-ilu")
    except ValueError as e:
        print(e)

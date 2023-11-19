def prnt_vhcl(vhcl_mps):
    print(vhcl_mps)


def s(inp, inp_index):
    if [inp[0], inp[3]] == [0, 0]:
        if [inp[1], inp[2]] == [0, 0]:
            s = [0, 1], [0, 0]
        return s


if __name__ == "__main__":
    vhcl_mps = 20.0
    prnt_vhcl(vhcl_mps)

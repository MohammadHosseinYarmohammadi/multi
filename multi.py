

from  gooey import Gooey, GooeyParser

@Gooey(program_name="multy tab")

def main():
    parser = GooeyParser()
    sp = parser.add_subparsers(dest = "forfunction")
    ap = sp.add_parser("intro")
    ag = ap.add_argument_group("introduction")
    ag.add_argument("description", widget = "Textarea", gooey_options = {"initial_value": "for test"})

    ap1 = sp.add_parser("printparser")
    ap1.add_argument("inputvar", help= "plz input", default= "adad:")

    args = parser.parse_args()
    return args
import os


def load_json(path: str) -> str:
    """Loads json file with data of the rule seed
    ### Parameters
    `path: str`

    ### Returns
    `str`
        String with content of json file.
    """
    with open(
        os.path.join(
            os.path.dirname(path),
            'files',
            os.path.basename(path).replace('py', 'json')
        )
    ) as f:
        data = f.read()
    return data

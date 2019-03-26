args_converter = lambda row_index, rec: \
        {'text': rec['text'],
         'size_hint_y': None,
         'height': 25,
         'cls_dicts': [{'cls': ListItemButton,
                        'kwargs': {'text': rec['text']}},
                       {'cls': ListItemLabel,
                        'kwargs': {'text': rec['text'],
                                   'is_representing_cls': True}},
                       {'cls': ListItemButton,
                        'kwargs': {'text': rec['text']}}]}
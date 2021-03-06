data files
----------
constellations.json -> Constellation data
constellations.bounds.json -> Constellation boundaries
constellations.lines.json -> Constellation lines

proposed in-memory dictionary structure for all constellation instances once we read in the above files
-------------------------------------------------------------------------------------------------------

constellations = {
    "unique_three_letter_id_per_constellation": {
        "properties": {
                    "desig": "And",
                    "gen": "Andromedae",
                    "name": "Andromeda"
                },
        "location": {
            "geometry": {
                "coordinates": [
                    0.75,
                    43
                ],
                "type": "Point"
            }
        },
        "bounds": {
            "geometry": {
                "coordinates": [
                    [
                        [
                            -15.5347,
                            35.1682
                        ],
                        [
                            -15.6571,
                            53.168
                        ],
                        [
                            -8.5471,
                            53.187
                        ],
                        [
                            -8.5343,
                            50.687
                        ],
                        [
                            -4.7294,
                            50.6929
                        ],
                        [
                            -4.7239,
                            48.6929
                        ],
                        [
                            4.1464,
                            48.6949
                        ],
                        [
                            4.1433,
                            46.6949
                        ],
                        [
                            14.7761,
                            46.6758
                        ],
                        [
                            14.7889,
                            48.6757
                        ],
                        [
                            18.5884,
                            48.6633
                        ],
                        [
                            18.6059,
                            50.6632
                        ],
                        [
                            22.4079,
                            50.6479
                        ],
                        [
                            26.9685,
                            50.6257
                        ],
                        [
                            26.9314,
                            47.6258
                        ],
                        [
                            32.6215,
                            47.5928
                        ],
                        [
                            32.6738,
                            51.0926
                        ],
                        [
                            39.8855,
                            51.0424
                        ],
                        [
                            39.6793,
                            37.2932
                        ],
                        [
                            31.8711,
                            37.3471
                        ],
                        [
                            31.8543,
                            35.5971
                        ],
                        [
                            22.9108,
                            35.6453
                        ],
                        [
                            22.8974,
                            33.6454
                        ],
                        [
                            12.4431,
                            33.6819
                        ],
                        [
                            12.4135,
                            24.4319
                        ],
                        [
                            14.4241,
                            24.4266
                        ],
                        [
                            14.4148,
                            21.6766
                        ],
                        [
                            3.7399,
                            21.6952
                        ],
                        [
                            3.7406,
                            22.6952
                        ],
                        [
                            2.61,
                            22.6958
                        ],
                        [
                            2.6128,
                            28.6958
                        ],
                        [
                            1.6062,
                            28.696
                        ],
                        [
                            1.607,
                            32.0294
                        ],
                        [
                            -2.1713,
                            32.0285
                        ],
                        [
                            -2.1719,
                            32.7785
                        ],
                        [
                            -5.9508,
                            32.7746
                        ],
                        [
                            -5.9558,
                            35.1913
                        ],
                        [
                            -15.5347,
                            35.1682
                        ]
                    ]
                ],
                "type": "Polygon"
            }
        },
        "lines": {
            "geometry": {
                "coordinates": [
                    [
                        [
                            30.9748,
                            42.3297
                        ],
                        [
                            17.433,
                            35.6206
                        ],
                        [
                            9.832,
                            30.861
                        ],
                        [
                            2.0969,
                            29.0904
                        ]
                    ],
                    [
                        [
                            14.3017,
                            23.4176
                        ],
                        [
                            11.8347,
                            24.2672
                        ],
                        [
                            9.6389,
                            29.3118
                        ],
                        [
                            9.832,
                            30.861
                        ],
                        [
                            9.2202,
                            33.7193
                        ],
                        [
                            -5.4658,
                            43.2681
                        ],
                        [
                            -14.5197,
                            42.326
                        ]
                    ],
                    [
                        [
                            -5.4658,
                            43.2681
                        ],
                        [
                            -4.8979,
                            44.3339
                        ],
                        [
                            -5.609,
                            46.4581
                        ]
                    ],
                    [
                        [
                            17.433,
                            35.6206
                        ],
                        [
                            14.1884,
                            38.4993
                        ],
                        [
                            12.4535,
                            41.0789
                        ],
                        [
                            17.3755,
                            47.2418
                        ],
                        [
                            24.4982,
                            48.6282
                        ]
                    ],
                    [
                        [
                            -4.8979,
                            44.3339
                        ],
                        [
                            -3.4915,
                            46.4203
                        ]
                    ]
                ],
                "type": "MultiLineString"
            }
        }
    }
}
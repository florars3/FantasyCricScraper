FantasyCricScraper
It scrapes the scorecard information from the cricinfo.com/matchid.
Example:
http://www.espncricinfo.com/indian-premier-league-2016/engine/match/980919.html


[![Build Status][travis-image]][travis-url]

FantasyCricScraper scrapes information from the cricinfo website and then
displays into a dictionary which looks like the following:

Bowler list: [{'PlayerName': 'SandeepSharma', 'Points': 72}, {'PlayerName': 'KJAbbott', 'Points': 33}, {'PlayerName': 'ARPatel', 'Points': 11}, {'PlayerName': 'PSahu', 'Points': 16}, {'PlayerName': 'MMSharma', 'Points': 98}, {'PlayerName': 'GJMaxwell', 'Points': 18}, {'PlayerName': 'ISharma', 'Points': 15}, {'PlayerName': 'AnkitSharma', 'Points': 38}, {'PlayerName': 'RAshwin', 'Points': 18}, {'PlayerName': 'MAshwin', 'Points': 90}, {'PlayerName': 'IKPathan', 'Points': 13}, {'PlayerName': 'NLTCPerera', 'Points': -8}]

Batsman Points: [{'PlayerName': 'AM Rahane', 'Points': 9.0}, {'PlayerName': 'F du Plessis', 'Points': 92.0}, {'PlayerName': 'KP Pietersen', 'Points': 20.0}, {'PlayerName': 'NLTC Perera', 'Points': 8.0}, {'PlayerName': 'SPD Smith', 'Points': 53.0}, {'PlayerName': 'MS Dhoni', 'Points': 1.0}, {'PlayerName': 'IK Pathan', 'Points': 2.0}, {'PlayerName': 'R Ashwin', 'Points': 1.0}, {'PlayerName': 'M Vijay', 'Points': 82.0}, {'PlayerName': 'M Vohra', 'Points': 81.0}, {'PlayerName': 'SE Marsh', 'Points': 4.0}, {'PlayerName': 'DA Miller', 'Points': 7.0}, {'PlayerName': 'GJ Maxwell', 'Points': 61.0}, {'PlayerName': 'WP Saha', 'Points': 4.0}]

## Installation

OS X & Linux:

```sh
 1) Download chromedriver.exe

 2) Download Selenium and add the libraries to your project
 
 3) Edit fantasyCricScraper.py to have the path to the chromedriver

```

## Meta

Ripudaman Flora – flora_ripudaman@hotmail.com

Distributed under the MIT license. See ``LICENSE`` for more information.

[https://github.com/florars3/FantasyCricScraper](https://github.com/florars3/FantasyCricScraper)

[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square
[npm-url]: https://npmjs.org/package/datadog-metrics
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics

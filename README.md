# ViPNet Coordinator HW Config Generator
ViPNet Coordinator HW configuration files generator, based on data stored in Excel

## Getting Started
ViPNet Coordinator HW Config Generator is a python script. So to use it you need python 3 (3.5+) to be installed.
It support only `xlsx` format, not `xls`. 

###  Prerequisites
To run this script you need:
* python 3.5+
* openpyxl (lib to communicate with Excel-files)
* glog (logging lib) 

If you use pip
```bash
pip install openpyxl
pip install glog
```

### Run
To run  script you need to provide path to excel file you want to use to generate configuration files to
For example:

```bash
python3 main.py -f ./hw-data.xlsx
```

### Structure of data in Excel file

Structure of Excel file can be found in `cfg-data-template.xlsx`

## Authors

* **Ivan Kovalev** - *Initial work* - [sector84](https://github.com/sector84/)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


# ViPNet Coordinator HW Config Generator
ViPNet Coordinator HW configuration files generator, based on data stored in Excel

## Getting Started
ViPNet Coordinator HW Config Generator is a python script. So to use it you need python 3 (3.5+) to be installed.
ViPNet Coordinator HW configuration files generator supports only `xlsx` format, not `xls`.
To generate output configuration files application uses one of templates stored in `cfg_templates` directory
Config Templates is a `Jinja-templates` 

###  Prerequisites
To run this script you need:
* python 3.5+
* openpyxl (lib to communicate with Excel-files)
* glog (logging lib) 
* jinja2 (lib for templating)

If you use pip, just run following commands
```bash
pip install openpyxl
pip install glog
pip install jinja2
```

### Run
To run  script you need to provide path to excel file you want to use to generate configuration files to
For example:

```bash
python3 main.py -f ./_data_/HW.xlsx -t hw_v1.j2
```

### Structure of data in Excel file

Structure of Excel file can be found in `cfg-data-template.xlsx`

## Authors

* **Ivan Kovalev** - *Initial work* - [sector84](https://github.com/sector84/)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


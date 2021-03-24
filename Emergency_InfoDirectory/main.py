import pandas as pd

def main():
    bazar_csv =pd.read_csv('bazar.csv')
    firestation_csv =pd.read_csv('fire_station.csv')

    # print(bazar_csv)
    # print(firestation_csv)

    # for i in range (len(firestation_csv)):
    #     fire_station = FireStation(firestation_id = firestation_csv['ID'][i],
    #     firestation_name = firestation_csv['Name'][i],
    #     contact_no = firestation_csv['Contact No'][i],
    #     address = firestation_csv['Address'][i],
    #     subdistrict = firestation_csv['Subdistrict'][i],
    #     district = firestation_csv['District'][i],
    #     division = firestation_csv['Division'][i])

    #print(bazar_csv['ID'][i],bazar_csv['Name'][i],bazar_csv['Contact No'][i],bazar_csv['Address'][i],bazar_csv['Union'][i],bazar_csv['Subdistrict'][i],bazar_csv['District'][i],bazar_csv['Division'][i])


if __name__ == '__main__':
    main()

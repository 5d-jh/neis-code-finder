import csv from "csv-parser";
import { createReadStream } from "fs";

export interface SchoolInfo {
    address: string,
    code: string,
    name: string
};

export const getData = (searchString: string): Promise<{
    data: Array<SchoolInfo>,
    isAll: boolean
}> => new Promise((resolve, reject) => {
    if (searchString.length === 0) {
        return resolve({
            data: [],
            isAll: true
        })
    }

    const searchResult = Array<SchoolInfo>();

    createReadStream("data.csv")
    .pipe(csv())
    .on("data", row => {
        if (searchResult.length >= 20) {
            return resolve({
                data: searchResult,
                isAll: false
            });
        }

        const schoolName: string = row[3];

        if (schoolName.includes(searchString)) {
            searchResult.push({
                address: String(row[1]),
                code: String(row[2]),
                name: String(row[3])
            });
        }
    })
    .on("end", () => {
        resolve({
            data: searchResult,
            isAll: true
        });
    });
});

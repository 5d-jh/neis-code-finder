import { AzureFunction, Context, HttpRequest } from "@azure/functions";
import { getData } from "../get-data";


const httpTrigger: AzureFunction = async function (context: Context, req: HttpRequest): Promise<void> {
    const query = req.query.q;

    if (!query) {
        context.res = {
            status: 400,
            body: JSON.stringify({
                school_infos: [],
                server_message: "학교명이 없습니다."
            }),
            headers: { "Content-Type": "application/json;" }
        };
        return;
    }

    const { data, isAll } = await getData(query);

    context.res = {
        status: 200,
        body: JSON.stringify({
            school_infos: data,
            server_message: {
                all_loaded: isAll
            }
        }),
        headers: { "Content-Type": "application/json;" }
    };
};

export default httpTrigger;

import { AzureFunction, Context, HttpRequest } from "@azure/functions"
import nunjucks from "nunjucks";
import { getData } from "../get-data";

const httpTrigger: AzureFunction = async function (context: Context, req: HttpRequest): Promise<void> {
    const query: string = req.query.q || '';
    
    const { data, isAll } = await getData(query);

    nunjucks.configure("app/")
    const nj = nunjucks.render("./index.html", {
        query,
        school_infos: data,
        is_all: isAll
    });

    context.res = {
        status: 200,
        body: nj,
        headers: { "Content-Type": "text/html;" }
    };
};

export default httpTrigger;

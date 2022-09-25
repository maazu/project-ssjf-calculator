const API_URL = "http://3.236.248.167:8000";

export async function calApi(ApiBody) {
  let object = {
    status: "error",
    data: "",
    message: `Error `,
  };
  try {
    let response = await fetch(`${API_URL}/cal/compute/`, {
      method: "POST",
      body: ApiBody,
      redirect: "follow",
    });
    console.log("response", response);
    let json = await response.json();
    if (response.ok) {
      object.status = "success";
      object.data = json;
      object.message = `operation completed successfully`;
    } else {
      if (Array.isArray(json)) {
        let string = JSON.stringify(values[0]);
        object.message += ", " + string.slice(1, string.length - 1);
      } else if (typeof json === "object" && json !== null) {
        object.message += ", " + Object.values(json)[0];
      } else if (typeof json === "string") {
        object.message += ", " + json;
      }
    }
    return object;
  } catch (error) {
    return object;
  }
}

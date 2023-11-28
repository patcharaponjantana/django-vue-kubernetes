import axios from "axios";

export const base_API_URL = import.meta.env.VITE_BACKEND_URL;
// export const FRONTEND_CALLBACK: string = process.env.FRONTEND_CALLBACK || "";

// Note: jwt token authen did not implement yet!
export const ACC_TOKEN_NAME = "acc_token";
export const ACC_TOKEN_EXPIRED = "acc_token_expired";
export const REFS_TOKEN_NAME = "refs_token";

const isRequired = (param: any) => {
  /* 
        Function Required param 
        Usage: 
    */
  throw new Error(`${param} is required.`);
};

const API_ErrorHandler = {
  REST_API(error: object) {
    console.log("Error:", error);
    return error;
  },
};

var headers = {
  "Content-Type": "application/json"
};

export const Axios_instance = axios.create({
  baseURL: base_API_URL,
  headers: headers,
  timeout: 100000
});

const Axios = {
  async get(url = isRequired("url")) {
    return Axios_instance.get(url)
      .then((response) => response)
      .catch((error) => error.response);
  },
  async post(url = isRequired("url")) {
    return Axios_instance.post(url)
      .then((response) => response)
      .catch((error) => error.response);
  },
};

const Axios_Auth = {
  async get(url: string = isRequired("url"), body?: object) {
    try {
      const accessToken = localStorage.getItem(ACC_TOKEN_NAME);
      const response = await Axios_instance.get(url, {
        headers: {
          Authorization: `Bearer ${accessToken}`,
          "Content-Type": "application/json",
        },
      });
      return response;
    } catch (error: any) {
      return error.response;
    }
  },
  async post(url: string = isRequired("url"), body?: object) {
    try {
      const accessToken = localStorage.getItem(ACC_TOKEN_NAME);
      const response = await Axios_instance.post(url, body, {
        headers: {
          Authorization: `Bearer ${accessToken}`,
          "Content-Type": "application/json",
        },
      });

      return response;
    } catch (error: any) {
      return error.response;
    }
  },
  delete() {},
  put() {},
  patch() {},
};

export { Axios, Axios_Auth };


import { defineStore } from 'pinia'

import { Axios_Auth } from "../services/axios.service";

const DEFAULT_STATE: any = {
  location: [],
  searchResult: [],
};

export const useMainStore = defineStore({
  id: 'counter',
  state: () => ({...DEFAULT_STATE}),
  getters: {
    // getLocation: (state) => state.location,
    // getSearch: (state) => state.searchResult,
  },
  actions: {
    async checkUserSession(status: number, data?: any) {
      // check if any problem with request 

      // if (status === 401 && data?.code === "token_not_valid") {
      //   this.setIsLogout();
      //   setTimeout(() => {
      //     window.location.reload();
      //   }, 480);
      // }
    },
    async getLocationList() {
      let { data, status } = await Axios_Auth.get("/api/location/");
      if (status === 200) {
        this.location = data.results;
      } else {
        await this.checkUserSession(status, data);
      }
    },
    async getSearchResult(source: number, destination: number, date: string) {
      let { data, status } = await Axios_Auth.get(`/api/boat-schedule/?from_location__name=${source}&to_location__name=${destination}&departure_time__date=${date}`);
      if (status === 200) {
        this.searchResult = data.results;
      } else {
        await this.checkUserSession(status, data);
      }
    }
  }
})
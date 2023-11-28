import { createWebHistory, createRouter } from "vue-router";
import type { RouteRecordRaw } from "vue-router";

const routes: RouteRecordRaw[] = [
  {
    path: "/",
    name: "home",
    components: {
      default: () => import("./pages/Home.vue"),
    },
  },
  {
    path: "/search",
    name: "search",
    components: {
      default: () => import("./pages/Search.vue"),
    },
  },
  {
    path: "/booking",
    name: "booking",
    components: {
      default: () => import("./pages/Booking.vue"),
    },
  },
  {
    path: "/booking-success",
    name: "booking-success",
    components: {
      default: () => import("./pages/BookingSuccess.vue"),
    },
  },
//   {
//     path: "/project",
//     redirect: "/"
//   },
//   {
//     path: "/project/:id",
//     // alias: "/project",
//     name: "project-id",
//     components: {
//       default: () => import("@pages/project/Index.vue"),
//       Navigation: () => import("@components/Core/Navigation/Navigation.vue"),
//     },
//   },
//   {
//     path: "/callback/:catchAll(.*)*",
//     name: "Callback",
//     components: { default: () => import("@pages/Callback.vue") },
//   },
//   {
//     path: "/login",
//     name: "login",
//     components: {
//       default: () => import("@pages/Login.vue"),
//     },
//   },
];

const AppRouter = createRouter({
  history: createWebHistory(),
  routes,
});

export default AppRouter;


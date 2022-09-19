# build stage
FROM node:18-alpine as build-stage
WORKDIR /app
COPY ./package*.json ./
RUN npm install
COPY . .
RUN npm run build
# ENV VUE_APP_API_URL=backend
# ENV VUE_APP_API_PORT=7777

# production stage
FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html
COPY ./nginx/ /etc/nginx/conf.d/
EXPOSE 80
ENTRYPOINT ["/etc/nginx/conf.d/docker-entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]

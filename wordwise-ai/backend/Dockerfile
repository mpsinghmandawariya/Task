FROM node:22-bookworm-slim
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends python3 make g++ && rm -rf /var/lib/apt/lists/*
COPY package*.json ./
RUN npm install --omit=dev
COPY src ./src
RUN mkdir -p /data && chown -R node:node /app /data
ENV NODE_ENV=production
USER node
EXPOSE 5000
CMD ["node","src/server.js"]

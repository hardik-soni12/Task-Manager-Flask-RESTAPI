FROM node:20-alpine
WORKDIR /app

# 1. Install dependencies first (for better caching)
COPY package*.json ./
RUN npm install

# 2. Copy code and build
COPY . .
RUN npm run build


ENV NODE_ENV=production \
    PORT=3000

RUN cp -r /app/.next/static /app/.next/standalone/.next/static
RUN cp -r /app/public /app/.next/standalone/public

# 4. Final Execution
EXPOSE 3000
WORKDIR /app/.next/standalone
CMD ["node", "server.js"]
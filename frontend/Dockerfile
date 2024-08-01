# Establece la imagen base
FROM node:16

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el package.json y el package-lock.json
COPY package*.json ./

# Limpia la caché de npm y luego instala las dependencias
RUN npm cache clean --force && npm install --legacy-peer-deps

# Copia el resto de los archivos de la aplicación al directorio de trabajo
COPY . .

# Compila la aplicación
RUN npm run build

# Expone el puerto en el que la aplicación estará corriendo
EXPOSE 3000

# Comando para ejecutar la aplicación
CMD ["npm", "start"]

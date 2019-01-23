FROM nginx:alpine

# Set the file maintainer (your name - the file's author)
MAINTAINER Bob

# Turn off daemon mode
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

# Copy nginx config
COPY nginx_proxy.conf /etc/nginx/conf.d/default.conf
        
# Define default command.
CMD ["nginx"]

# Expose ports.
EXPOSE 80
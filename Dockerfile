FROM somniholic/docker-stella:python36

# install our code
ADD . /code/

ADD requirements.txt /code/

# RUN pip install on app requirements
RUN pip install -r /code/requirements.txt

# sort out permissions
RUN chown -R www-data:www-data /code

# setup nginx config
RUN ln -s /code/nginx-app.conf /etc/nginx/sites-enabled/
RUN ln -s /code/supervisor-app.conf /etc/supervisor/conf.d/

WORKDIR /code

# collectstatic
# RUN mkdir -p /code/weird_math_competition/collected_static
# RUN python /code/weird_math_competition/manage.py collectstatic --noinput

# make directory media if not exists
RUN mkdir -p /code/weird_math_competition/media

EXPOSE 80 22

CMD ["supervisord", "-n"]
"""
Meta related routes
"""
# Bridges software forges to create a distributed software development environment
# Copyright © 2021 Aravinth Manivannan <realaravinth@batsense.net>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
from flask import Blueprint, jsonify, request
from dynaconf import settings

from interface.auth import PublicKey

bp = Blueprint("META", __name__, url_prefix="/_ff/interface/")

VERSIONS = ["1"]
payload = {"versions": VERSIONS}


@bp.route("versions", methods=["GET"])
def versions():
    """
    get supported interface protocol versions
    """
    return jsonify(payload)


@bp.route("key", methods=["GET"])
def get_verify_key():
    """get public key"""
    return PublicKey(key=settings.PRIVATE_KEY).to_resp()

import React, { Component, useEffect } from 'react'
import WishList from "./WishList"
import { makeStyles } from '@material-ui/core/styles';
import axios from "axios";

export default class WishCarousel extends Component {
    constructor(props) {
        super(props);
        this.state = {
        data: [],
        loaded: false,
        placeholder: "Loading"
        };
    }

    componentDidMount() {
        axios
        .get('wishes/' + this.props.url)
        .then(resp => {
            if (resp.status > 400) {
                return this.setState( () => {
                    return { placeholder: "Something's fucky" }
                })
            }
            console.log(resp)
            return resp.data;
        })
        .then(data => {
            this.setState(() => {
                return {
                    data,
                    loaded: true
                }
            })
        })
    };

    render() {
        return (
            <WishList data={this.state.data} />
        );
    }
}